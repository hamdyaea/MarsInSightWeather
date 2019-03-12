#!/usr/bin/python3

# Developer : Hamdy Abou El Anein

from easygui import *
import wget
import json
import os

def parser():
    with open('rawdata', 'r') as f:
        mars = json.load(f)

        sol_keys=mars["sol_keys"]
        sol_keys_new=sol_keys[-1]
        ActuSeason = mars[sol_keys_new]["Season"]
        Last_temp=mars[sol_keys_new]["AT"]
        last_date=mars[sol_keys_new]["First_UTC"]

        sol_keys_new1 = sol_keys[-2]
        Last_temp1 = mars[sol_keys_new1]["AT"]
        last_date1 = mars[sol_keys_new1]["First_UTC"]

        sol_keys_new2 = sol_keys[-3]
        Last_temp2 = mars[sol_keys_new2]["AT"]
        last_date2 = mars[sol_keys_new2]["First_UTC"]

        sol_keys_new3 = sol_keys[-4]
        Last_temp3 = mars[sol_keys_new3]["AT"]
        last_date3 = mars[sol_keys_new3]["First_UTC"]

        sol_keys_new4 = sol_keys[-5]
        Last_temp4 = mars[sol_keys_new4]["AT"]
        last_date4 = mars[sol_keys_new4]["First_UTC"]

        sol_keys_new5 = sol_keys[-6]
        Last_temp5 = mars[sol_keys_new5]["AT"]
        last_date5 = mars[sol_keys_new5]["First_UTC"]

        sol_keys_new6 = sol_keys[-7]
        Last_temp6 = mars[sol_keys_new6]["AT"]
        last_date6 = mars[sol_keys_new6]["First_UTC"]


        image = "weather.png"
        msg = ((("Mars InSight at Elysium Planitia latests weather report \nThe temperature is updated from Mars everyday\n\n\nLast sol for insight on Mars : ")+str(sol_keys_new))+str(("\n\nLast signal date : ")+str(last_date[:10]))+str(("\n\nLast signal time : ")+str(last_date[-9:-1]))+str(("\n\nMinimum Temperature : ")+str(Last_temp['mn']))+str(("\n\nMaximum Temperature : ") + str(Last_temp['mx']))+str(("\n\nAverage Temperature : ") + str(Last_temp['av'])+str(("\n\nAverage minimum temperature for the last 7 days : ")+str(((Last_temp['mn'])+(Last_temp1['mn'])+(Last_temp2['mn'])+(Last_temp3['mn'])+(Last_temp4['mn'])+(Last_temp5['mn'])+(Last_temp6['mn']))/7))+str(("\n\nAverage maximum temperature for the last 7 days : ") + str(((Last_temp['mx']) + (Last_temp1['mx']) + (Last_temp2['mx']) + (Last_temp3['mx']) + (Last_temp4['mx']) + (Last_temp5['mx']) + (Last_temp6['mx'])) / 7)))+("\n\nCurrent season on Mars : ")+str(ActuSeason))
        choices = ["Ok"]
        reply = buttonbox(msg, image=image, choices=choices)


filePath = "rawdata"

if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("")

url = ("https://mars.nasa.gov/rss/api/?feed=weather&category=insight&feedtype=json&ver=1.0")
filename = wget.download(url,out="rawdata")

filePath1 = "weather.png"

if os.path.exists(filePath1):
    os.remove(filePath1)
else:
    print("")

url1 = ("https://mars.nasa.gov/rss/api/images/insight_marsweather_white.png")
filename1 = wget.download(url1,out="weather.png")

cmd = "convert -resize 25%  weather.png weather.png"
os.system(cmd)


parser()



