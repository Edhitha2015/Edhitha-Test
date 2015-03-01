import sys
import ntpath
import glob
from itertools import chain
from PIL.ExifTags import TAGS
from PIL import Image
import csv
from datetime import datetime as dt




def latlon(img):
    info = img._getexif()
    decoded = dict((TAGS.get(key, key), value) for key, value in info.items())
    info = {
       
        "lat": None,
        "lon": None,
       # "timestamp": None,
        "altitude": None,
    }
   
    if not decoded.get('GPSInfo'):
        return info
    lat = [float(x) / float(y) for x, y in decoded['GPSInfo'][2]]
    lon = [float(x) / float(y) for x, y in decoded['GPSInfo'][4]]
    alt = float(decoded['GPSInfo'][6][0]) / float(decoded['GPSInfo'][6][1])
    timestamp = decoded['DateTimeOriginal']
    
    info['lat'] = (lat[0] + lat[1] / 60)
    info['lon'] = (lon[0] + lon[1] / 60)
    #info['timestamp'] = dt.strptime(
     #   timestamp,
      #  "%Y:%m:%d %H:%M:%S").strftime("%Y/%m/%d %H:%M:%S")
    info['altitude'] = alt
    
    if decoded['GPSInfo'][1] == "S":
        info['lat'] *= -1
    if decoded['GPSInfo'][3] == "W":
        info['lon'] *= -1
 
    if decoded['GPSInfo'][5] == 1:
        info['altitude'] *= -1
    return info




'''if __name__ == "__main__":
    image = Image.open("test-images/DSC_0884.JPG")
   
    #print exif_data
    print latlon(image)'''
