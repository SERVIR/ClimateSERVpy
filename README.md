# ClimateServ API Access

This is a simple package to access the [ClimateSERV API](https://climateserv.servirglobal.net/) 
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
            * 25th percentile
                * Variable: CHIRPS_GEFS_precip_25
            * 75th percentile
                * Variable: CHIRPS_GEFS_precip_75
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
    * Variable: Seasonal_Forecast
        * SeasonalEnsemble Variable: ens01 thru ens10
        * seasonal_variable: Temperature or Precipitation
* IMERG 1 Day
    * Variable: IMERG
* Evaporative Stress Index
    * ESI 4 week
        * Variable: ESI_4
    * ESI 12 week
        * Variable: ESI_12
    
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
SeasonalEnsemble = 'ens07'
SeasonalVariable = 'Precipitation'
Outfile = 'out.csv'

climateserv.api.request_data(DatasetType, OperationType, 
             EarliestDate, LatestDate,GeometryCoords, 
             SeasonalEnsemble, SeasonalVariable,Outfile)
</pre>