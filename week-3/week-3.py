import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["results"]
with open ("data.csv","w",encoding="utf-8")as file:
    for att in clist:
        attfile=att["file"]
        attfile_split=attfile.split("https")
        attfile1=attfile_split
        file.write(att["stitle"]+","+att["address"]+","+att["longitude"]+","+"https"+attfile1[1]+"\n")
            
    
