# ClimateServ API Access


[![Python: 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![SERVIR: Global](https://img.shields.io/badge/SERVIR-Global-green)](https://servirglobal.net)

This is a python package to access the [ClimateSERV API](https://climateserv.servirglobal.net/)
you can install using conda or pip:
* conda install -c servir climateserv
* pip install climateserv

## Current supported operations:
* Timeseries CSV 
    * Variables
        * Average
        * Min
        * Max
* Download Zip file of tifs
    * Variable
        * Download
* Download Zip file containing a NetCDF
    * Variable
        * NetCDF


## Current supported datasets:
We are moving to the dataset numbers to match the way ClimateSERV handles the datasets.  We will continue to 
support the prior named variables for the datasets, but recommend updating to use the integer values.  This will 
allow any future datasets that are added to be accessed by their ID found on ClimateSERV even if this documentation 
is not yet updated.  

* UCSB CHIRPS Rainfall: 0
* eMODIS West Africa NDVI: 1
* eMODIS East Africa NDVI: 2
* eMODIS Southern Africa NDVI: 5
* IMERG 1 Day (late): 26
* eMODIS Central Asia NDVI: 28
* Evaporative Stress Index (ESI) 4 week: 29
* CHIRPS GEFS Anomalies: 31
* CHIRPS GEFS Precipitation: 32
* Evaporative Stress Index (ESI) 12 week: 33
* NASA-USDA Enhanced SMAP Global Soil moisture profile: 37
* NASA-USDA Enhanced SMAP Global Surface soil moisture: 38
* NASA-USDA Enhanced SMAP Global Surface soil moisture anomaly: 39
* NASA-USDA Enhanced SMAP Global Subsurface soil moisture: 40
* NASA-USDA Enhanced SMAP Global Subsurface soil moisture anomaly: 41
* UCSB CHIRP Rainfall: 90
* IMERG 1 Day (early): 91
* NSIDC SMAP Sentinel 1Km: 541
* NSIDC SMAP Sentinel 1Km 15 day: 542
* LIS-modeled Evapotranspiration: 661
* LIS-modeled Baseflow: 662
* LIS-Modeled Runoff: 663
* LIS-Modeled Soil Moisture 0-10cm: 664
* LIS-Modeled Soil Moisture 10-40cm: 665
* LIS-Modeled Soil Moisture 40-100cm: 666
* LIS-Modeled Soil Moisture 100-200cm: 667


NMME forecast datasets:

## CCSM4
* NMME ccsm4 ens01 Temperature: 6
* NMME ccsm4 ens01 Precipitation: 7
* NMME ccsm4 ens02 Temperature: 8
* NMME ccsm4 ens02 Precipitation: 9
* NMME ccsm4 ens03 Temperature: 10
* NMME ccsm4 ens03 Precipitation: 11
* NMME ccsm4 ens04 Temperature: 12
* NMME ccsm4 ens04 Precipitation: 13
* NMME ccsm4 ens05 Temperature: 14
* NMME ccsm4 ens05 Precipitation: 15
* NMME ccsm4 ens06 Temperature: 16
* NMME ccsm4 ens06 Precipitation: 17
* NMME ccsm4 ens07 Temperature: 18
* NMME ccsm4 ens07 Precipitation: 19
* NMME ccsm4 ens08 Temperature: 20
* NMME ccsm4 ens08 Precipitation: 21
* NMME ccsm4 ens09 Temperature: 22
* NMME ccsm4 ens09 Precipitation: 23
* NMME ccsm4 ens10 Temperature: 24
* NMME ccsm4 ens10 Precipitation: 25

## CSFV2
* NMME cfsv2 ens01 Temperature: 42
* NMME cfsv2 ens01 Precipitation: 43
* NMME cfsv2 ens02 Temperature: 44
* NMME cfsv2 ens02 Precipitation: 45
* NMME cfsv2 ens03 Temperature: 46
* NMME cfsv2 ens03 Precipitation: 47
* NMME cfsv2 ens04 Temperature: 48
* NMME cfsv2 ens04 Precipitation: 49
* NMME cfsv2 ens05 Temperature: 50
* NMME cfsv2 ens05 Precipitation: 51
* NMME cfsv2 ens06 Temperature: 52
* NMME cfsv2 ens06 Precipitation: 53
* NMME cfsv2 ens07 Temperature: 54
* NMME cfsv2 ens07 Precipitation: 55
* NMME cfsv2 ens08 Temperature: 56
* NMME cfsv2 ens08 Precipitation: 57
* NMME cfsv2 ens09 Temperature: 58
* NMME cfsv2 ens09 Precipitation: 59
* NMME cfsv2 ens10 Temperature: 60
* NMME cfsv2 ens10 Precipitation: 61
* NMME cfsv2 ens11 Temperature: 62
* NMME cfsv2 ens11 Precipitation: 63
* NMME cfsv2 ens12 Temperature: 64
* NMME cfsv2 ens12 Precipitation: 65
* NMME cfsv2 ens13 Temperature: 66
* NMME cfsv2 ens13 Precipitation: 67
* NMME cfsv2 ens14 Temperature: 68
* NMME cfsv2 ens14 Precipitation: 69
* NMME cfsv2 ens15 Temperature: 70
* NMME cfsv2 ens15 Precipitation: 71
* NMME cfsv2 ens16 Temperature: 72
* NMME cfsv2 ens16 Precipitation: 73
* NMME cfsv2 ens17 Temperature: 74
* NMME cfsv2 ens17 Precipitation: 75
* NMME cfsv2 ens18 Temperature: 76
* NMME cfsv2 ens18 Precipitation: 77
* NMME cfsv2 ens19 Temperature: 78
* NMME cfsv2 ens19 Precipitation: 79
* NMME cfsv2 ens20 Temperature: 80
* NMME cfsv2 ens20 Precipitation: 81
* NMME cfsv2 ens21 Temperature: 82
* NMME cfsv2 ens21 Precipitation: 83
* NMME cfsv2 ens22 Temperature: 84
* NMME cfsv2 ens22 Precipitation: 85
* NMME cfsv2 ens23 Temperature: 86
* NMME cfsv2 ens23 Precipitation: 87
* NMME cfsv2 ens24 Temperature: 88
* NMME cfsv2 ens24 Precipitation: 89


    
# Sample Usage

This is sample code to produce a time series csv using the CentralAsia_eModis dataset.  If you were to choose the OperationType of Download you would need to change the Outfile from .csv to .zip If you would like the data returned as a json object to a variable set Outfile to 'memory_object' and create a variable to hold the return from the climateserv.api.request_data call. 
<pre>
import climateserv.api

x = 81.27   
y = 29.19

GeometryCoords = [[x-.01,y+.01],[x+.01, y+.01],
                  [x+.01, y-.01],[x-.01,y-.01],[x-.01,y+.01]]
                  
DatasetType = 28
OperationType = 'Average'
EarliestDate = '01/03/2018'
LatestDate = '03/16/2018'
SeasonalEnsemble = '' # Leave empty when using the new integer dataset IDs
SeasonalVariable = '' # Leave empty when using the new integer dataset IDs
Outfile = 'out.csv'

climateserv.api.request_data(DatasetType, OperationType, 
             EarliestDate, LatestDate,GeometryCoords, 
             SeasonalEnsemble, SeasonalVariable,Outfile)
</pre>


## License and Distribution

ClimateSERVpy is distributed by SERVIR under the terms of the MIT License. See
[LICENSE](https://github.com/SERVIR/ClimateSERVpy/blob/master/LICENSE) in this directory for more information.

## Privacy & Terms of Use

ClimateSERVpy abides to all of SERVIR's privacy and terms of use as described
at [https://servirglobal.net/Privacy-Terms-of-Use](https://servirglobal.net/Privacy-Terms-of-Use).
