#網路連線
import urllib.request as request
import json
import time
import re
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
#串接、擷取公開資料
attractionlist=data["result"]["results"]
with open("data.csv", "w",encoding="utf-8") as file:
    for attraction in attractionlist:
        xpostDate = attraction["xpostDate"]
        title_date = "2014/12/31"
        formatted_xpostDate = time.strptime(xpostDate, "%Y/%m/%d")
        formatted_title_date = time.strptime(title_date, "%Y/%m/%d")
        
        if (xpostDate>title_date):
            file.write(attraction["stitle"]+","+attraction["address"][5:8]+","+attraction["longitude"]+","+attraction["latitude"]+","+"https://"+attraction["file"].split("https://")[1]+"\n")