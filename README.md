# ClimateServ API Access


[![Python: 3.7](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![SERVIR: Global](https://img.shields.io/badge/SERVIR-Global-green)](https://servirglobal.net)

This is a python package to access the [ClimateSERV API](https://climateserv.servirglobal.net/) 
you can install using pip:
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
* CHIRPS
    * Rainfall
        * Variable: CHIRPS
    * GEFS
        * Anomalies
            * Variable: CHIRPS_GEFS_anom
        * Precipitation 
            * Mean
                * Variable: CHIRPS_GEFS_precip_mean
* CHIRP
    * Rainfall
        * Variable: CHIRP
* eMODIS
    * Central Asia NDVI
        * Variable: CentralAsia_eMODIS
    * East Africa NDVI
        * Variable: EastAfrica_eMODIS
    * Southern Africa NDVI
        * Variable: SouthAfrica_eMODIS
    * West Africa NDVI
        * Variable: WestAfrica_eMODIS
* Seasonal_Forecast
    * Variable: CCSM4
        * SeasonalEnsemble Variable: ens01 thru ens10
        * seasonal_variable: Temperature or Precipitation
  * Variable: CFSV2
      * SeasonalEnsemble Variable: ens01 thru ens24
      * seasonal_variable: Temperature or Precipitation
* IMERG 1 Day (late)
    * Variable: IMERG
* IMERG 1 Day (early)
    * Variable: IMERG_early
* Evaporative Stress Index
    * ESI 4 week
        * Variable: ESI_4
    * ESI 12 week
        * Variable: ESI_12
* NASA-USDA Enhanced SMAP Global Soil Moisture Data
    * Soil moisture profile
      * Variable: USDA_SMAP
    * Surface soil moisture
      * Variable: USDA_SSM
    * Surface soil moisture anomaly
        * Variable: USDA_SSMA
    * Subsurface soil moisture
        * Variable: USDA_SSSM
    * Subsurface soil moisture anomaly
        * Variable: USDA_SSSMA

    
# Sample Usage

This is sample code to produce a time series csv using the CentralAsia_eModis dataset.  If you were to choose the OperationType of Download you would need to change the Outfile from .csv to .zip If you would like the data returned as a json object to a variable set Outfile to 'memory_object' and create a variable to hold the return from the climateserv.api.request_data call. 
<pre>
import climateserv.api

x = 81.27   
y = 29.19

GeometryCoords = [[x-.01,y+.01],[x+.01, y+.01],
                  [x+.01, y-.01],[x-.01,y-.01],[x-.01,y+.01]]
                  
DatasetType = 'CentralAsia_eMODIS'
OperationType = 'Average'
EarliestDate = '01/03/2018'
LatestDate = '03/16/2018'
SeasonalEnsemble = '' # only used for Seasonal_Forecast
SeasonalVariable = '' # only used for Seasonal_Forecast
Outfile = 'out.csv'

climateserv.api.request_data(DatasetType, OperationType, 
             EarliestDate, LatestDate,GeometryCoords, 
             SeasonalEnsemble, SeasonalVariable,Outfile)
</pre>


## License and Distribution

ClimateSERVpy is distributed by SERVIR under the terms of the MIT License. See
[LICENSE](https://github.com/SERVIR/ClimateSERV2/blob/master/LICENSE) in this directory for more information.

## Privacy & Terms of Use

ClimateSERVpy abides to all of SERVIR's privacy and terms of use as described
at [https://servirglobal.net/Privacy-Terms-of-Use](https://servirglobal.net/Privacy-Terms-of-Use).