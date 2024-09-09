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
        if operation_type == 7:
            value_key = "FileGenerationSuccess"

        csv_header_string_list.append(date_key)
        csv_header_string_list.append(value_key)

        for currentGranule in job_data['data']:
            current_date = "NULL"
            current_value = "NULL"
            if not (operation_type == 6 or operation_type == 7):
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
    print_me(f"New Script Run, Dataset: {data_set_type}")

    base_url = "https://climateserv.servirglobal.net/api/"
    submit_url = base_url + "submitDataRequest/"
    progress_url = base_url + "getDataRequestProgress/"
    data_url = base_url + "getDataFromRequest/"

    g_obj = {"type": "Polygon", "coordinates": [], "properties": {}}
    try:
        g_obj['coordinates'].append(json.loads(str(geometry_coords)))
        geometry_json = json.dumps(g_obj)
        geometry_json_encoded = str(geometry_json.replace(" ", ""))
    except Exception as err:
        print_me("Error creating and encoding geometry_String parameter: " + str(err))
        return

    try:
        operation = request_utilities.get_operation_id(operation_type)
    except Exception as err:
        print_me("Error getting operation ID: " + str(err))
        return

    params = {
        "datatype": data_set_type,
        'seasonal_ensemble': seasonal_ensemble,
        'seasonal_variable': seasonal_variable,
        "begintime": earliest_date,
        "endtime": latest_date,
        "intervaltype": 0,
        "operationtype": operation,
        "dateType_Category": "default",
        "isZip_CurrentDataType": False,
        "geometry": geometry_json_encoded
    }

    try:
        # Make the POST request to submit the data request
        response = requests.post(submit_url, params=params)
        response.raise_for_status()
        request_id = json.loads(response.text)[0]  # Extract the request ID
        print(f"Data request submitted. Request ID: {request_id}")
    except Exception as err:
        print_me(f"Error submitting data request: {str(err)}")
        print_me(f"Response text: {response.text if response else 'No response'}")
        return

    # Check the progress of the data request
    while True:
        try:
            progress_response = requests.get(progress_url, params={"id": request_id})
            progress_response.raise_for_status()
            progress = json.loads(progress_response.text)[0]
        except Exception as err:
            print_me(f"Error checking progress: {str(err)}")
            break

        if progress == 100:  # Request is complete
            print(f"Data request is complete.")
            break
        elif progress == -1:  # Error occurred
            print(f"Error occurred while processing data request.")
            return
        else:
            print_me(f"Progress: {str(progress)}")

        time.sleep(1)  # Wait for 10 seconds before checking progress again

    the_url = f"https://climateserv.servirglobal.net/api/getFileForJobID/?id={request_id}"
    if operation in [6, 7]:
        local_file_name = outfile
        does_download_local_file_already_exist = os.path.isfile(local_file_name)

        try:
            # Download the file (and create it)
            download_file(the_url, local_file_name)
            print_me("Data for JobID: " + str(request_id) + " was downloaded to file: " + str(local_file_name))

            if does_download_local_file_already_exist:
                print_me("WARNING: -outfile param: " + str(
                    local_file_name) + " already exists. Download may fail or file may be overwritten.")
                print_me("VERBOSE: If there is an issue with your file, try the download link below.")
                print_me("   Download URL for JobID: " + str(request_id))
                print_me("     " + str(the_url))
                print_me("Note, download links are only valid for a short time (a few days)")
        except Exception as err:
            print_me(f"Error downloading file: {str(err)}")
        print_me("Exiting...")
        return

    try:
        data_response = requests.get(data_url, params={"id": request_id})
        data_response.raise_for_status()
        data_response_json = json.loads(data_response.text)
    except Exception as err:
        print_me(f"Error fetching data: {str(err)}")
        return

    if outfile == "memory_object":
        return data_response_json
    else:
        try:
            print_me("Attempting to write CSV Data to: " + outfile)
            single_data_set, row_headings, failed_file_list = get_csv_ready_processed_dataset(data_response_json,
                                                                                              operation)
            job_header_info = ['JobID', request_id]

            with open(outfile, 'a', newline='') as the_file:
                f = csv.writer(the_file)
                f.writerow(job_header_info)
                f.writerow(row_headings)
                for row in single_data_set:
                    f.writerow([row[row_headings[0]], row[row_headings[1]]])

            print_me("CSV Data Written to: " + str(outfile))
            print_me("Exiting...")
            return
        except Exception as e:
            print_me("Failed to create the CSV file output. Attempting to write the CSV data to the console: " + str(e))
            try:
                print_me("_CSV_DATA_START")
                print_me("rowHeadings: " + str(row_headings))
                print_me("singleDataSet: " + str(single_data_set))
                print_me("_CSV_DATA_END")
                print_me("Exiting...")
                return
            except Exception as e2:
                print_me("Could not write CSV data to the console... " + str(e2))
                print_me("Exiting...")
                return
