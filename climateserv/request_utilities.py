def get_dataset_id(dataset_type, seasonal_ensemble, seasonal_variable):
    if dataset_type == "CHIRPS":
        return 0
    if dataset_type == "WestAfrica_eMODIS":
        return 1
    if dataset_type == "EastAfrica_eMODIS":
        return 2
    if dataset_type == "SouthAfrica_eMODIS":
        return 5
    if dataset_type == "Seasonal_Forecast" or dataset_type == "CCSM4":
        if seasonal_ensemble == "ens01":
            if seasonal_variable == "Temperature":
                return 6
            if seasonal_variable == "Precipitation":
                return 7
        if seasonal_ensemble == "ens02":
            if seasonal_variable == "Temperature":
                return 8
            if seasonal_variable == "Precipitation":
                return 9
        if seasonal_ensemble == "ens03":
            if seasonal_variable == "Temperature":
                return 10
            if seasonal_variable == "Precipitation":
                return 11
        if seasonal_ensemble == "ens04":
            if seasonal_variable == "Temperature":
                return 12
            if seasonal_variable == "Precipitation":
                return 13
        if seasonal_ensemble == "ens05":
            if seasonal_variable == "Temperature":
                return 14
            if seasonal_variable == "Precipitation":
                return 15
        if seasonal_ensemble == "ens06":
            if seasonal_variable == "Temperature":
                return 16
            if seasonal_variable == "Precipitation":
                return 17
        if seasonal_ensemble == "ens07":
            if seasonal_variable == "Temperature":
                return 18
            if seasonal_variable == "Precipitation":
                return 19
        if seasonal_ensemble == "ens08":
            if seasonal_variable == "Temperature":
                return 20
            if seasonal_variable == "Precipitation":
                return 21
        if seasonal_ensemble == "ens09":
            if seasonal_variable == "Temperature":
                return 22
            if seasonal_variable == "Precipitation":
                return 23
        if seasonal_ensemble == "ens10":
            if seasonal_variable == "Temperature":
                return 24
            if seasonal_variable == "Precipitation":
                return 25
    if dataset_type == "IMERG":
        return 26
    if dataset_type == "CentralAsia_eMODIS":
        return 28
    if dataset_type == "ESI_4":
        return 29
    if dataset_type == "CHIRPS_GEFS_anom":
        return 31
    if dataset_type == "CHIRPS_GEFS_precip_mean":
        return 32
    if dataset_type == "ESI_12":
        return 33
    if dataset_type == "CHIRPS_GEFS_precip_25":
        return 35
    if dataset_type == "CHIRPS_GEFS_precip_75":
        return 36
    if dataset_type == "USDA_SMAP":
        return 37
    if dataset_type == "USDA_SSM":
        return 38
    if dataset_type == "USDA_SSMA":
        return 39
    if dataset_type == "USDA_SSSM":
        return 40
    if dataset_type == "USDA_SSSMA":
        return 41
    if dataset_type == "CFSV2":
        if seasonal_ensemble == "ens01":
            if seasonal_variable == "Temperature":
                return 42
            if seasonal_variable == "Precipitation":
                return 43
        if seasonal_ensemble == "ens02":
            if seasonal_variable == "Temperature":
                return 44
            if seasonal_variable == "Precipitation":
                return 45
        if seasonal_ensemble == "ens03":
            if seasonal_variable == "Temperature":
                return 46
            if seasonal_variable == "Precipitation":
                return 47
        if seasonal_ensemble == "ens04":
            if seasonal_variable == "Temperature":
                return 48
            if seasonal_variable == "Precipitation":
                return 49
        if seasonal_ensemble == "ens05":
            if seasonal_variable == "Temperature":
                return 50
            if seasonal_variable == "Precipitation":
                return 51
        if seasonal_ensemble == "ens06":
            if seasonal_variable == "Temperature":
                return 52
            if seasonal_variable == "Precipitation":
                return 53
        if seasonal_ensemble == "ens07":
            if seasonal_variable == "Temperature":
                return 54
            if seasonal_variable == "Precipitation":
                return 55
        if seasonal_ensemble == "ens08":
            if seasonal_variable == "Temperature":
                return 56
            if seasonal_variable == "Precipitation":
                return 57
        if seasonal_ensemble == "ens09":
            if seasonal_variable == "Temperature":
                return 58
            if seasonal_variable == "Precipitation":
                return 59
        if seasonal_ensemble == "ens10":
            if seasonal_variable == "Temperature":
                return 60
            if seasonal_variable == "Precipitation":
                return 61
        if seasonal_ensemble == "ens11":
            if seasonal_variable == "Temperature":
                return 62
            if seasonal_variable == "Precipitation":
                return 63
        if seasonal_ensemble == "ens12":
            if seasonal_variable == "Temperature":
                return 64
            if seasonal_variable == "Precipitation":
                return 65
        if seasonal_ensemble == "ens13":
            if seasonal_variable == "Temperature":
                return 66
            if seasonal_variable == "Precipitation":
                return 67
        if seasonal_ensemble == "ens14":
            if seasonal_variable == "Temperature":
                return 68
            if seasonal_variable == "Precipitation":
                return 69
        if seasonal_ensemble == "ens15":
            if seasonal_variable == "Temperature":
                return 70
            if seasonal_variable == "Precipitation":
                return 71
        if seasonal_ensemble == "ens16":
            if seasonal_variable == "Temperature":
                return 72
            if seasonal_variable == "Precipitation":
                return 73
        if seasonal_ensemble == "ens17":
            if seasonal_variable == "Temperature":
                return 74
            if seasonal_variable == "Precipitation":
                return 75
        if seasonal_ensemble == "ens18":
            if seasonal_variable == "Temperature":
                return 76
            if seasonal_variable == "Precipitation":
                return 77
        if seasonal_ensemble == "ens19":
            if seasonal_variable == "Temperature":
                return 78
            if seasonal_variable == "Precipitation":
                return 79
        if seasonal_ensemble == "ens20":
            if seasonal_variable == "Temperature":
                return 80
            if seasonal_variable == "Precipitation":
                return 81
        if seasonal_ensemble == "ens21":
            if seasonal_variable == "Temperature":
                return 82
            if seasonal_variable == "Precipitation":
                return 83
        if seasonal_ensemble == "ens22":
            if seasonal_variable == "Temperature":
                return 84
            if seasonal_variable == "Precipitation":
                return 85
        if seasonal_ensemble == "ens23":
            if seasonal_variable == "Temperature":
                return 86
            if seasonal_variable == "Precipitation":
                return 87
        if seasonal_ensemble == "ens24":
            if seasonal_variable == "Temperature":
                return 88
            if seasonal_variable == "Precipitation":
                return 89

    if dataset_type == "CHIRP":
        return 90
    if dataset_type == "IMERG_early":
        return 91
    return -1


def get_operation_id(operation_type):
    if operation_type == "Average":
        return 5
    if operation_type == "Max":
        return 0
    if operation_type == "Min":
        return 1
    if operation_type == "Download":
        return 6
    if operation_type == "NetCDF":
        return 7
    # if we got this far, there was an issue looking up the operation id
    return -1