def get_dataset_id(dataset_type, seasonal_ensemble=None, seasonal_variable=None):
    # Mapping of non-seasonal datasets
    dataset_ids = {
        "CHIRPS": 0,
        "WestAfrica_eMODIS": 1,
        "EastAfrica_eMODIS": 2,
        "SouthAfrica_eMODIS": 5,
        "IMERG": 26,
        "CentralAsia_eMODIS": 28,
        "ESI_4": 29,
        "CHIRPS_GEFS_anom": 31,
        "CHIRPS_GEFS_precip_mean": 32,
        "ESI_12": 33,
        "CHIRPS_GEFS_precip_25": 35,
        "CHIRPS_GEFS_precip_75": 36,
        "USDA_SMAP": 37,
        "USDA_SSM": 38,
        "USDA_SSMA": 39,
        "USDA_SSSM": 40,
        "USDA_SSSMA": 41,
        "CHIRP": 90,
        "IMERG_early": 91
    }

    # Mapping for seasonal datasets
    seasonal_mapping = {
        "ens01": {"Temperature": 6, "Precipitation": 7},
        "ens02": {"Temperature": 8, "Precipitation": 9},
        "ens03": {"Temperature": 10, "Precipitation": 11},
        "ens04": {"Temperature": 12, "Precipitation": 13},
        "ens05": {"Temperature": 14, "Precipitation": 15},
        "ens06": {"Temperature": 16, "Precipitation": 17},
        "ens07": {"Temperature": 18, "Precipitation": 19},
        "ens08": {"Temperature": 20, "Precipitation": 21},
        "ens09": {"Temperature": 22, "Precipitation": 23},
        "ens10": {"Temperature": 24, "Precipitation": 25},
        "ens11": {"Temperature": 62, "Precipitation": 63},
        "ens12": {"Temperature": 64, "Precipitation": 65},
        "ens13": {"Temperature": 66, "Precipitation": 67},
        "ens14": {"Temperature": 68, "Precipitation": 69},
        "ens15": {"Temperature": 70, "Precipitation": 71},
        "ens16": {"Temperature": 72, "Precipitation": 73},
        "ens17": {"Temperature": 74, "Precipitation": 75},
        "ens18": {"Temperature": 76, "Precipitation": 77},
        "ens19": {"Temperature": 78, "Precipitation": 79},
        "ens20": {"Temperature": 80, "Precipitation": 81},
        "ens21": {"Temperature": 82, "Precipitation": 83},
        "ens22": {"Temperature": 84, "Precipitation": 85},
        "ens23": {"Temperature": 86, "Precipitation": 87},
        "ens24": {"Temperature": 88, "Precipitation": 89}
    }

    if dataset_type in dataset_ids:
        return dataset_ids[dataset_type]

    if dataset_type in ["Seasonal_Forecast", "CCSM4", "CFSV2"]:
        if seasonal_ensemble in seasonal_mapping and seasonal_variable in seasonal_mapping[seasonal_ensemble]:
            if dataset_type == "CFSV2" and seasonal_ensemble in [f"ens{i:02d}" for i in range(1, 11)]:
                base_offset = 36
            else:
                base_offset = 0
            return seasonal_mapping[seasonal_ensemble][seasonal_variable] + base_offset

    return -1


def get_operation_id(operation_type):
    operation_ids = {
        "Average": 5,
        "Max": 0,
        "Min": 1,
        "Download": 6,
        "NetCDF": 7
    }

    return operation_ids.get(operation_type, -1)