import time
import urllib
import urllib.request
import json
import os
import logging
import csv
import climateserv.request_utilities as request_utilities
import requests


def print_me(message):
    print(message)
    try:
        logging.info(message)
    except Exception as e:
        print(str(e))
        pass


def get_request_data_url(base_url, job_id):
    return base_url + "getDataFromRequest?a=3&id=" + str(job_id)


def get_file_for_job_id_url(base_url, job_id):
    return base_url + "getFileForJobID?a=4&id=" + str(job_id)


def get_server_response(the_url):
    try:
        time.sleep(1)
        return json.load(urllib.request.urlopen(the_url, timeout=30))
    except Exception as e:
        print_me(e)


def verify_response(response):
    if 'errorMsg' in response:
        error_message = response['errorMsg']
        print_me("**** SERVER RESPONDED WITH AN ERROR ")
        print_me("**** The server responded to your request with an error message.")
        print_me("**** Error Message: " + error_message)
        return False
    else:
        return True


def return_error_message():
    print_me("ERROR.  There was an error with this job.")
    print_me("(The error may have been caused by an error on the server.)")
    print_me(
        "Double check the parameters you set and try again.  If the error persists, please contact the "
        "ClimateSERV Staff and be sure to send the parameters you used. Thank you!")
    return {}


def get_job_id_from_response(response):
    try:
        return response[0]
    except Exception as e:
        print_me("get_ServerReturn_JobID_FromResponse: Something went wrong..Generic Catch All Error. " + str(e))
        return -1


def get_job_progress_value(response):
    try:
        return response[0]
    except Exception as e:
        # Something went wrong, Catch all
        print_me("get_JobProgressValue_FromResponse: Something went wrong..Generic Catch All Error. " + str(e))
        return -1.0  # Default, 'error' code for jobstatus


def check_job_progress(job_id, base_url):
    return int(get_job_progress_value(
        get_server_response(
            base_url + 'getDataRequestProgress?a=2&id=' + str(job_id))
    ))


def get_job_cycle_progress(job_id, base_url):
    is_in_cycle = True
    cycle_complete_count = 0
    job_status = "unset"
    num_of_cycles_to_try = 1800
    last_reported_progress = 0

    while is_in_cycle:
        # get Job Progress value
        current_job_progress = check_job_progress(job_id, base_url)
        print_me("Current Job Progress: " + str(current_job_progress) + ".  JobID: " + str(job_id))
        time.sleep(1)

        # Process Job Status
        if current_job_progress == 100:
            job_status = "complete"
            is_in_cycle = False
        elif current_job_progress == -1:
            job_status = "error_generic"
            is_in_cycle = False
        else:
            job_status = "in_progress"
            is_in_cycle = True

        if current_job_progress > last_reported_progress:
            # still processing, reset cycle_complete_count
            last_reported_progress = current_job_progress
            cycle_complete_count = 0
        # Should we bail out of this loop?
        if cycle_complete_count > num_of_cycles_to_try:
            job_status = "error_timeout"
            is_in_cycle = False

        cycle_complete_count += 1

        # For long wait times, echo the cycle
        if cycle_complete_count % 50 == 0:
            print_me("Still working.... Cycle: " + str(cycle_complete_count))

    # Process return (did the job fail or succeed..)
    print_me("Result of Job Status Cycle: " + str(job_status))
    if job_status == "complete":
        return True
    else:
        return False


def sort_job_data(job_data):
    try:
        converted_epoch_times_list = job_data['data']
        for x in range(0, len(converted_epoch_times_list)):
            converted_epoch_times_list[x]['epochTime'] = int(converted_epoch_times_list[x]['epochTime'])
        sorted_job_data = sorted(converted_epoch_times_list, key=lambda k: k['epochTime'])
        return {'data': sorted_job_data}
    except Exception as e:
        print_me(str(e))
        return job_data


def get_csv_ready_processed_dataset(job_data, operation_type):
    job_data = sort_job_data(job_data)
    ret_list = []
    file_failed_list = []
    csv_header_string_list = []
    try:
        # Set the Key from the operation Type
        date_key = "date"
        value_key = "value"
        if operation_type == 0:
            value_key = "max"
        if operation_type == 1:
            value_key = "min"
        if operation_type == 5:
            value_key = "avg"
        if operation_type == 6:
            value_key = "FileGenerationSuccess"

        csv_header_string_list.append(date_key)
        csv_header_string_list.append(value_key)

        for currentGranule in job_data['data']:
            current_date = "NULL"
            current_value = "NULL"
            if not (operation_type == 6):
                # For non download types
                current_date = str(currentGranule[date_key])
                current_value = str(currentGranule['value'][value_key])
            else:
                # For download types
                current_date = str(currentGranule[date_key])
                current_value = str(currentGranule['value'])
                if current_value == '0':
                    file_failed_list.append(current_date)

            ret_list.append({
                date_key: current_date,
                value_key: current_value
            })

    except Exception as e:
        print_me("get_CSV_Ready_Processed_Dataset: Something went wrong..Generic Catch All Error. " + str(e))

    return ret_list, csv_header_string_list, file_failed_list


def process_job_controller(config_obj):
    job_operation_id = request_utilities.get_operation_id(config_obj['operation_type'])
    job_dataset_id = request_utilities.get_dataset_id(config_obj['dataset_type'],
                                                      config_obj['seasonal_ensemble'],
                                                      config_obj['seasonal_variable'])

    # Validation
    if job_dataset_id == -1:
        print_me(
            "ERROR.  DatasetID not found.  Check your input params to ensure the DatasetType value is correct.  (Case "
            "Sensitive), refer to the readme example at https://github.com/SERVIR/ClimateSERVpy")

        return -1
    if job_operation_id == -1:
        print_me(
            "ERROR.  OperationID not found.  Check your input params to ensure the OperationType value is correct.  ("
            "Case Sensitive), refer to the readme example at https://github.com/SERVIR/ClimateSERVpy")
        return -1

    g_obj = {"type": "Polygon", "coordinates": [], "properties": {}}
    g_obj['coordinates'].append(config_obj['geometry_coords'])
    geometry_json = json.dumps(g_obj)
    try:
        geometry_json_encoded = str(geometry_json.replace(" ", ""))
    except Exception as err:
        print_me("Error Creating and encoding geometry_String parameter" + str(err))
        geometry_json_encoded = str(geometry_json.replace(" ", ""))

    url = config_obj['base_url'] + "submitDataRequest/"
    post_data = {
        'datatype': str(job_dataset_id),
        'intervaltype': 0,
        'operationtype': job_operation_id,
        'begintime': str(config_obj['earliest_date']),
        'endtime': str(config_obj['latest_date']),
        'geometry': geometry_json_encoded
    }

    x = requests.post(url, data=post_data, json=post_data)

    new_job_response = json.loads(x.text)

    if verify_response(new_job_response):
        the_job_id = get_job_id_from_response(new_job_response)

        # Validate the JobID
        if the_job_id == -1:
            print_me("Something went wrong submitting the job.  Waiting for a few seconds and trying one more time")
            time.sleep(3)
            x = requests.post(url, data=post_data, json=post_data)
            print(x.text)
            new_job_response = json.loads(x.text)
            if verify_response(new_job_response):
                the_job_id_second_try = get_job_id_from_response(new_job_response)
                if the_job_id_second_try == -1:
                    print_me("Job Submission second failed attempt.  Bailing Out.")
                    return {}
                else:
                    the_job_id = the_job_id_second_try

        print_me("New Job Submitted to the Server: New JobID: " + str(the_job_id))

        # Enter the loop waiting on the progress.
        is_job_success = get_job_cycle_progress(the_job_id, config_obj['base_url'])

        # Report Status to the user (console)
        print_me("Job, " + str(the_job_id) + " is done, did it succeed? : " + str(is_job_success))

        # If it succeeded, get data
        if is_job_success:
            get_job_data_response = get_server_response(
                config_obj['base_url'] + "getDataFromRequest?a=3&id=" + str(the_job_id))

            csv_ready_data_obj, csv_header_list, failed_file_list = get_csv_ready_processed_dataset(
                get_job_data_response, job_operation_id)

            # If file download job, generate the file download link.
            download_link = "NA"
            if job_operation_id == 6 or job_operation_id == 7:
                download_link = get_file_for_job_id_url(config_obj['base_url'], the_job_id)

            return {
                "ServerJobID": the_job_id,
                "JobData_ServerResponse_JSON": get_job_data_response,
                "csvHeaderList": csv_header_list,
                "csvWriteReady_DataObj": csv_ready_data_obj,
                "downloadLink": download_link,
                "rawData_FailedDatesList": failed_file_list
            }

        else:
            return_error_message()

        return_error_message()
    else:
        return_error_message()


def process_requests(config_obj):
    jobs_data_list = []

    print_me("About to process scripted job item now.")
    try:
        # Execute Job
        current_job_return_data = process_job_controller(config_obj)

        # Store Job Return Data along with original Config Item

        jobs_data_list.append({
            "JobReturnData": current_job_return_data,
            "JobConfigData": config_obj
        })
    except Exception as e:
        print_me(
            "ERROR: Something went wrong!!       There and can mean that there is currently an issue with the "
            "server.  Please try again later.  If the error persists, please contact the ClimateSERV staff.")
        print_me("  This is a generic catch all error that could have multiple possible causes.")
        print_me("     Possible causes may include:")
        print_me("       Issues with your connection to the ClimateSERV server")
        print_me("       Issues with your connection to the Internet")
        print_me("       Invalid input parameters from the configuration file or command line")
        print_me("       Interruptions of service with the ClimateSERV Service")
        print_me(str(e))

    print_me("=======================================================")
    return jobs_data_list


def download_file(url_to_file, local_file_name):
    f = urllib.request.urlopen(url_to_file)
    print_me("Downloading file.  This may take a few minutes..")
    with open(local_file_name, "wb") as local_file:
        local_file.write(f.read())


def request_data(data_set_type,
                 operation_type, earliest_date,
                 latest_date, geometry_coords,
                 seasonal_ensemble, seasonal_variable,
                 outfile):
    print_me("New Script Run")

    # Make the request, get the data!
    request_config = {
        'dataset_type': str(data_set_type),
        'operation_type': str(operation_type),
        'seasonal_ensemble': str(seasonal_ensemble),
        'seasonal_variable': str(seasonal_variable),
        'earliest_date': str(earliest_date),
        'latest_date': str(latest_date),
        'geometry_coords': json.loads(str(geometry_coords)),
        'base_url': 'https://climateserv.servirglobal.net/api/',
        'outfile': outfile
    }
    job_data = process_requests(request_config)

    # Check Type (Is this a download job or a script job?)
    if request_config['operation_type'] == 'Download' or request_config['operation_type'] == 'NetCDF':
        # Do the download stuff
        try:
            local_file_name = request_config['outfile']

            the_url = job_data[0]['JobReturnData']['downloadLink']
            the_job_id = job_data[0]['JobReturnData']['ServerJobID']
            does_download_local_file_already_exist = os.path.isfile(local_file_name)

            # Download the file (and create it)
            download_file(the_url, local_file_name)

            print_me("Data for JobID: " + str(the_job_id) + " was downloaded to file: " + str(local_file_name))

            if does_download_local_file_already_exist:
                print_me("WARNING: -outfile param: " + str(
                    local_file_name) + " already exists.  Download may fail or file may be overwritten.")
                print_me("VERBOSE: If there is an issue with your file, try the download link below.")
                print_me("   Download URL for JobID: " + str(the_job_id))
                print_me("     " + str(the_url))
                print_me("Note, download links are only valid for a short time (a few days)")
            print_me("Exiting...")
            return
        except Exception as e:
            print_me("Failed to download the file, Attempting to write the download URL to the console. " + str(e))
            try:
                the_url = job_data[0]['JobReturnData']['downloadLink']
                the_job_id = job_data[0]['JobReturnData']['ServerJobID']
                print_me("Download URL for JobID: " + str(the_job_id))
                print_me(str(the_url))
                print_me(
                    "Copy and paste this URL into your web browser to manually download the file.  It will be only be "
                    "available for a few days!")
                print_me("Exiting...")
                return
            except Exception as e2:
                print_me("Could not get download link to write to the console... Exiting...")
                print_me(str(e2))
                return
    elif str(request_config['outfile']) == "memory_object":
        return job_data[0]['JobReturnData']['JobData_ServerResponse_JSON']
    else:
        try:
            print_me("Attempting to write CSV Data to: " + str(request_config['outfile']))
            job_header_info = ['JobID', job_data[0]['JobReturnData']['ServerJobID']]
            row_headings = job_data[0]['JobReturnData']['csvHeaderList']
            single_data_set = job_data[0]['JobReturnData']['csvWriteReady_DataObj']

            my_csv_file_name = request_config['outfile']

            the_file = open(my_csv_file_name, 'a')
            f = csv.writer(the_file)
            f.writerow(job_header_info)
            f.writerow(row_headings)
            for row in single_data_set:
                f.writerow([
                    row[row_headings[0]],
                    row[row_headings[1]]
                ])

            the_file.close()
            print_me("CSV Data Written to: " + str(my_csv_file_name))
            print_me("Exiting...")
            print_me("")
            return
        except Exception as e:
            print_me("Failed to create the CSV file output.  "
                     "Attempting to write the CSV data to the console: " + str(e))
            try:
                row_headings = job_data[0]['JobReturnData']['csvHeaderList']
                single_data_set = job_data[0]['JobReturnData']['csvWriteReady_DataObj']
                print_me("_CSV_DATA_START")
                print_me("rowHeadings: " + str(row_headings))
                print_me("singleDataSet: " + str(single_data_set))
                print_me("_CSV_DATA_END")
                print_me("Exiting...")
                return
            except Exception as e2:
                print_me("Could not write CSV data to the console... " + str(e2))
                print_me("Exiting...")
                print_me("")
                return
