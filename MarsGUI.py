#!/usr/bin/python3

# Developer : Hamdy Abou El Anein

from easygui import *
import wget
import json
import os
import sys


def parser():
    with open("rawdata", "r") as f:
        mars = json.load(f)

        sol_keys = mars["sol_keys"]
        sol_keys_new = sol_keys[-1]

        try:
            ActuSeason = mars[sol_keys_new]["Season"]
        except:
            ActuSeason = "No data"
        try:
            Last_temp = mars[sol_keys_new]["AT"]
        except:
            Last_temp = 0
        try:
            last_date = mars[sol_keys_new]["First_UTC"]
        except:
            last_date = 0

        try:
            sol_keys_new1 = sol_keys[-2]
            Last_temp1 = mars[sol_keys_new1]["AT"]
        except:
            sol_keys_new1 = 0
            Last_temp1 = 0

        try:
            sol_keys_new2 = sol_keys[-3]
            Last_temp2 = mars[sol_keys_new2]["AT"]
        except:
            sol_keys_new2 = 0
            Last_temp2 = 0

        try:
            sol_keys_new3 = sol_keys[-4]
            Last_temp3 = mars[sol_keys_new3]["AT"]
        except:
            sol_keys_new3 = 0
            Last_temp3 = 0

        try:
            sol_keys_new4 = sol_keys[-5]
            Last_temp4 = mars[sol_keys_new4]["AT"]
        except:
            sol_keys_new4 = 0
            Last_temp4 = 0

        try:
            sol_keys_new5 = sol_keys[-6]
            Last_temp5 = mars[sol_keys_new5]["AT"]
        except:
            sol_keys_new5 = 0
            Last_temp5 = 0

        try:
            sol_keys_new6 = sol_keys[-7]
            Last_temp6 = mars[sol_keys_new6]["AT"]
        except:
            sol_keys_new6 = 0
            Last_temp6 = 0

        try:
            average_seven_min = (
                (Last_temp["mn"])
                + (Last_temp1["mn"])
                + (Last_temp2["mn"])
                + (Last_temp3["mn"])
                + (Last_temp4["mn"])
                + (Last_temp5["mn"])
                + (Last_temp6["mn"])
            ) / 7
            average_seven_min_reduced = round(average_seven_min, 2)

            average_seven_max = (
                (Last_temp["mx"])
                + (Last_temp1["mx"])
                + (Last_temp2["mx"])
                + (Last_temp3["mx"])
                + (Last_temp4["mx"])
                + (Last_temp5["mx"])
                + (Last_temp6["mx"])
            ) / 7
            average_seven_max_reduced = round(average_seven_max, 2)

            AverageSevenDays = (
                Last_temp["av"]
                + Last_temp1["av"]
                + Last_temp2["av"]
                + Last_temp3["av"]
                + Last_temp4["av"]
                + Last_temp5["av"]
                + Last_temp6["av"]
            ) / 7
            AverageSevenDaysReduce = round(AverageSevenDays, 2)
        except:
            average_seven_min_reduced = 0
            average_seven_max_reduced = 0
            AverageSevenDaysReduce = 0

        try:
            LastMin = Last_temp["mn"]
            LastMinReduce = round(LastMin, 2)

            LastMax = Last_temp["mx"]
            LastMaxReduce = round(LastMax, 2)

            LastAv = Last_temp["av"]
            LastAvReduce = round(LastAv, 2)
        except:
            LastMinReduce = 0
            LastMaxReduce = 0
            LastAvReduce = 0

        # Wind speed

        try:
            Last_Wnd = mars[sol_keys_new]["HWS"]

            LastWindMin = Last_Wnd["mn"] * 3.6
            LastWindMinReduce = round(LastWindMin, 2)

            LastWindMax = Last_Wnd["mx"] * 3.6
            LastWindMaxReduce = round(LastWindMax, 2)

            LastWindav = Last_Wnd["av"] * 3.6
            LastWindavReduce = round(LastWindav, 2)
        except:
            LastWindMinReduce = 0
            LastWindMaxReduce = 0
            LastWindavReduce = 0

        try:
            Last_Wnd1 = mars[sol_keys_new1]["HWS"]
        except:
            Last_Wnd1 = 0
        try:
            Last_Wnd2 = mars[sol_keys_new2]["HWS"]
        except:
            Last_Wnd2 = 0
        try:
            Last_Wnd3 = mars[sol_keys_new3]["HWS"]
        except:
            Last_Wnd3 = 0
        try:
            Last_Wnd4 = mars[sol_keys_new4]["HWS"]
        except:
            Last_Wnd4 = 0
        try:
            Last_Wnd5 = mars[sol_keys_new5]["HWS"]
        except:
            Last_Wnd5 = 0
        try:
            Last_Wnd6 = mars[sol_keys_new6]["HWS"]
        except:
            Last_Wnd6 = 0

        try:
            AverageSevenDaysWind = (
                Last_Wnd["av"]
                + Last_Wnd1["av"]
                + Last_Wnd2["av"]
                + Last_Wnd3["av"]
                + Last_Wnd4["av"]
                + Last_Wnd5["av"]
                + Last_Wnd6["av"]
            ) / 7
            AverageSevenDaysWindReduce = round(AverageSevenDaysWind, 2)
        except:
            AverageSevenDaysWindReduce = 0

        # Pressure Atm
        try:
            Last_Pres = mars[sol_keys_new]["PRE"]

            LastPresMin = Last_Pres["mn"]
            LastPresMinReduce = round(LastPresMin, 2)

            LastPresMax = Last_Pres["mx"]
            LastPresMaxReduce = round(LastPresMax, 2)

            LastPresav = Last_Pres["av"]
            LastPresavReduce = round(LastPresav, 2)
        except:
            LastPresMinReduce = 0
            LastPresMaxReduce = 0
            LastPresavReduce = 0

        # GUI creation

        welcome = "Mars InSight at Elysium Planitia latests weather report"

        image = ("weatherOK.png", "insightLab.jpg")
        msg = (
            (welcome)
            + str("\nThe temperature is updated from Mars everyday")
            + str("\n\nLast sol for insight on Mars : ")
            + str(sol_keys_new)
            + str("          ")
            + str("Minimum Wind Speed ")
            + str(LastWindMinReduce)
            + str(" km/h")
            + str("\n\nLast signal date : ")
            + str(last_date[:10])
            + str("               ")
            + str("Maximum Wind Speed ")
            + str(LastWindMaxReduce)
            + str(" km/h")
            + str("\n\nLast signal time : ")
            + str(last_date[-9:-1])
            + str(" UTC")
            + str("             ")
            + str("Average Wind Speed ")
            + str(LastWindavReduce)
            + str(" km/h")
            + str("\n\nMinimum Temperature : ")
            + str(LastMinReduce)
            + str(" °C")
            + str("             ")
            + str("Average 7 days Wind Speed ")
            + str(AverageSevenDaysWindReduce)
            + str(" km/h")
            + str("\n\nMaximum Temperature : ")
            + str(LastMaxReduce)
            + str(" °C")
            + str("             ")
            + str("Minimum Air Pressure ")
            + str(LastPresMinReduce)
            + str(" Pa")
            + str("\n\nAverage Temperature : ")
            + str(LastAvReduce)
            + str(" °C")
            + str("             ")
            + str("Maximum Air Pressure ")
            + str(LastPresMaxReduce)
            + str(" Pa")
            + str("\n\nAverage 7 days temperature : ")
            + str(AverageSevenDaysReduce)
            + str(" °C")
            + str("      ")
            + str("     Average Air Pressure ")
            + str(LastPresavReduce)
            + str(" Pa")
            + str("\n\nAverage 7 days minimum temperature : ")
            + str(average_seven_min_reduced)
            + str(" °C")
            + str("\n\nAverage 7 days maximum temperature : ")
            + str(average_seven_max_reduced)
            + str(" °C")
            + ("\n\nCurrent season on Mars : ")
            + str((ActuSeason).title())
        )

        choices = ["Ok"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Ok":
            sys.exit(0)
        elif reply == "weatherOK.png":
            buttonbox(
                msg="Last Mars weather graph full size",
                image="weather.png",
                choices=["Close"],
            )
        elif reply == "insightLab.jpg":
            buttonbox(msg="Insight on Mars", image="insightLab.jpg", choices=["Close"])


filePath = "rawdata"

if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("")

url = (
    "https://mars.nasa.gov/rss/api/?feed=weather&category=insight&feedtype=json&ver=1.0"
)
filename = wget.download(url, out="rawdata")

filePath1 = "weather.png"

if os.path.exists(filePath1):
    os.remove(filePath1)
else:
    print("")

url1 = "https://mars.nasa.gov/rss/api/images/insight_marsweather_white.png"
filename1 = wget.download(url1, out="weather.png")

cmd = "convert -resize 25%  weather.png weatherOK.png"
os.system(cmd)


parser()
