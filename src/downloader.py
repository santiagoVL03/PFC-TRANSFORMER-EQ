from EQTransformer.utils.downloader import makeStationList, downloadMseeds
import os

# help(makeStationList)

MINLAT=35.50
MAXLAT=35.60
MINLON=-117.80
MAXLON=-117.40
STIME="2019-09-01 00:00:00.00"
ETIME="2019-09-03 00:00:00.00"

CHANLIST=["HH[ZNE]", "HH[Z21]", "BH[ZNE]", "EH[ZNE]", "SH[ZNE]", "HN[ZNE]", "HN[Z21]", "DP[ZNE]"]

json_basepath = os.path.join(os.getcwd(),"json/station_list.json")

makeStationList(json_path=json_basepath,
                  client_list=["SCEDC"],  
                  min_lat=MINLAT,
                  max_lat=MAXLAT,
                  min_lon=MINLON, 
                  max_lon=MAXLON,                      
                  start_time=STIME, 
                  end_time=ETIME,
                  channel_list=CHANLIST,
                  filter_network=["SY"],
                  filter_station=[])

downloadMseeds(client_list=["SCEDC", "IRIS"], 
          stations_json=json_basepath, 
          output_dir="downloads_mseeds", 
          start_time=STIME, 
          end_time=ETIME, 
          min_lat=MINLAT, 
          max_lat=MAXLAT, 
          min_lon=MINLON, 
          max_lon=MAXLON,
          chunk_size=1,
          channel_list=[],
          n_processor=2)