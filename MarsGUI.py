#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from easygui import *
import wget
import json
import os
import sys
import urllib.request
import logging

logging.basicConfig(
    filename="Mars.log",
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class RoverInsight:
    def __init__(self):
        self.mars
        self.sol_keys
        self.sol_keys_new
        self.ActuSeason
        self.Last_temp
        self.last_date
        self.sol_keys_new1
        self.Last_temp1
        self.sol_keys_new2
        self.Last_temp2
        self.sol_keys_new3
        self.Last_temp3
        self.sol_keys_new4
        self.Last_temp4
        self.sol_keys_new5
        self.Last_temp5
        self.sol_keys_new6
        self.Last_temp6
        self.average_seven_min
        self.average_seven_min_reduced
        self.average_seven_max_reduced
        self.average_seven_max
        self.AverageSevenDaysReduce
        self.AverageSevenDays
        self.average_seven_min_reduced
        self.average_seven_max_reduced
        self.LastMin
        self.LastMinReduce
        self.LastMax
        self.LastMaxReduce
        self.LastAv
        self.LastAvReduce
        self.Last_Wnd
        self.LastWindMin
        self.LastWindMinReduce
        self.LastWindMax
        self.LastWindMaxReduce
        self.LastWindav
        self.LastAvReduce
        self.Last_Wnd1
        self.Last_Wnd2
        self.Last_Wnd3
        self.Last_Wnd4
        self.Last_Wnd5
        self.Last_Wnd6
        self.AverageSevenDaysWind
        self.AverageSevenDaysWindReduce
        self.Last_Pres
        self.LastPresMin
        self.LastPresMinReduce
        self.LastPresMax
        self.LastPresMaxReduce
        self.LastPresav
        self.LastPresavReduce
        self.welcome
        self.image
        self.msg


def parser():
    RoverInsight.sol_keys = RoverInsight.mars["sol_keys"]
    RoverInsight.sol_keys_new = RoverInsight.sol_keys[-1]

    try:
        RoverInsight.ActuSeason = RoverInsight.mars[RoverInsight.sol_keys_new]["Season"]
        logging.info(RoverInsight.ActuSeason)
    except:
        RoverInsight.ActuSeason = "No data"
        logging.warning("RoverInsight.ActuSeason = No data")
    try:
        RoverInsight.Last_temp = RoverInsight.mars[RoverInsight.sol_keys_new]["AT"]
        logging.info(RoverInsight.Last_temp)
    except:
        RoverInsight.Last_temp = 0
        logging.warning("RoverInsight.Last_temp = 0")
    try:
        RoverInsight.last_date = RoverInsight.mars[RoverInsight.sol_keys_new][
            "First_UTC"
        ]
        logging.info(RoverInsight.last_date)
    except:
        RoverInsight.last_date = 0
        logging.warning("RoverInsight.last_date = 0")
    try:
        RoverInsight.sol_keys_new1 = RoverInsight.sol_keys[-2]
        RoverInsight.Last_temp1 = RoverInsight.mars[RoverInsight.sol_keys_new1]["AT"]
        logging.info(RoverInsight.sol_keys_new1 )
        logging.info(RoverInsight.Last_temp1)
    except:
        RoverInsight.sol_keys_new1 = 0
        RoverInsight.Last_temp1 = 0
        logging.warning("RoverInsight.sol_keys_new1 = 0")
        logging.warning("RoverInsight.Last_temp1 = 0")
    try:
        RoverInsight.sol_keys_new2 = RoverInsight.sol_keys[-3]
        RoverInsight.Last_temp2 = RoverInsight.mars[RoverInsight.sol_keys_new2]["AT"]
        logging.info(RoverInsight.sol_keys_new2)
        logging.info(RoverInsight.Last_temp2)
    except:
        RoverInsight.sol_keys_new2 = 0
        RoverInsight.Last_temp2 = 0
        logging.warning("RoverInsight.sol_keys_new2 = 0")
        logging.warning("RoverInsight.Last_temp2 = 0")
    try:
        RoverInsight.sol_keys_new3 = RoverInsight.sol_keys[-4]
        RoverInsight.Last_temp3 = RoverInsight.mars[RoverInsight.sol_keys_new3]["AT"]
        logging.info(RoverInsight.sol_keys_new3)
        logging.info(RoverInsight.Last_temp3)
    except:
        RoverInsight.sol_keys_new3 = 0
        RoverInsight.Last_temp3 = 0
        logging.warning("RoverInsight.sol_keys_new3 = 0")
        logging.warning("RoverInsight.Last_temp3 = 0")
    try:
        RoverInsight.sol_keys_new4 = RoverInsight.sol_keys[-5]
        RoverInsight.Last_temp4 = RoverInsight.mars[RoverInsight.sol_keys_new4]["AT"]
        logging.info(RoverInsight.sol_keys_new4)
        logging.info(RoverInsight.Last_temp4)
    except:
        RoverInsight.sol_keys_new4 = 0
        RoverInsight.Last_temp4 = 0
        logging.warning("RoverInsight.sol_keys_new4 = 0")
        logging.warning("RoverInsight.Last_temp4 = 0")
    try:
        RoverInsight.sol_keys_new5 = RoverInsight.sol_keys[-6]
        RoverInsight.Last_temp5 = RoverInsight.mars[RoverInsight.sol_keys_new5]["AT"]
        logging.info(RoverInsight.sol_keys_new5)
        logging.info(RoverInsight.Last_temp5)
    except:
        RoverInsight.sol_keys_new5 = 0
        RoverInsight.Last_temp5 = 0
        logging.warning("RoverInsight.sol_keys_new5 = 0")
        logging.warning("RoverInsight.Last_temp5 = 0")
    try:
        RoverInsight.sol_keys_new6 = RoverInsight.sol_keys[-7]
        RoverInsight.Last_temp6 = RoverInsight.mars[RoverInsight.sol_keys_new6]["AT"]
        logging.info(RoverInsight.sol_keys_new6)
        logging.info(RoverInsight.Last_temp6)
    except:
        RoverInsight.sol_keys_new6 = 0
        RoverInsight.Last_temp6 = 0
        logging.warning("RoverInsight.sol_keys_new6 = 0")
        logging.warning("RoverInsight.Last_temp6 = 0")
    try:
        RoverInsight.average_seven_min = (
            (RoverInsight.Last_temp["mn"])
            + (RoverInsight.Last_temp1["mn"])
            + (RoverInsight.Last_temp2["mn"])
            + (RoverInsight.Last_temp3["mn"])
            + (RoverInsight.Last_temp4["mn"])
            + (RoverInsight.Last_temp5["mn"])
            + (RoverInsight.Last_temp6["mn"])
        ) / 7
        RoverInsight.average_seven_min_reduced = round(
            RoverInsight.average_seven_min, 2
        )

        RoverInsight.average_seven_max = (
            (RoverInsight.Last_temp["mx"])
            + (RoverInsight.Last_temp1["mx"])
            + (RoverInsight.Last_temp2["mx"])
            + (RoverInsight.Last_temp3["mx"])
            + (RoverInsight.Last_temp4["mx"])
            + (RoverInsight.Last_temp5["mx"])
            + (RoverInsight.Last_temp6["mx"])
        ) / 7
        RoverInsight.average_seven_max_reduced = round(
            RoverInsight.average_seven_max, 2
        )

        RoverInsight.AverageSevenDays = (
            RoverInsight.Last_temp["av"]
            + RoverInsight.Last_temp1["av"]
            + RoverInsight.Last_temp2["av"]
            + RoverInsight.Last_temp3["av"]
            + RoverInsight.Last_temp4["av"]
            + RoverInsight.Last_temp5["av"]
            + RoverInsight.Last_temp6["av"]
        ) / 7
        RoverInsight.AverageSevenDaysReduce = round(RoverInsight.AverageSevenDays, 2)
        logging.info(RoverInsight.average_seven_min)
        logging.info(RoverInsight.average_seven_max)
        logging.info(RoverInsight.average_seven_max_reduced )
        logging.info(RoverInsight.AverageSevenDays)
    except:
        RoverInsight.average_seven_min_reduced = 0
        RoverInsight.average_seven_max_reduced = 0
        RoverInsight.AverageSevenDaysReduce = 0
        logging.warning("RoverInsight.average_seven_min_reduced = 0")
        logging.warning("RoverInsight.average_seven_max_reduced = 0")
        logging.warning("RoverInsight.AverageSevenDaysReduce = 0")
    try:
        RoverInsight.LastMin = RoverInsight.Last_temp["mn"]
        RoverInsight.LastMinReduce = round(RoverInsight.LastMin, 2)

        RoverInsight.LastMax = RoverInsight.Last_temp["mx"]
        RoverInsight.LastMaxReduce = round(RoverInsight.LastMax, 2)

        RoverInsight.LastAv = RoverInsight.Last_temp["av"]
        RoverInsight.LastAvReduce = round(RoverInsight.LastAv, 2)
        logging.info(RoverInsight.LastMinReduce)
        logging.info(RoverInsight.LastMaxReduce)
        logging.info(RoverInsight.LastAvReduce)
    except:
        RoverInsight.LastMinReduce = 0
        RoverInsight.LastMaxReduce = 0
        RoverInsight.LastAvReduce = 0
        logging.warning("RoverInsight.LastMinReduce = 0")
        logging.warning("RoverInsight.LastMaxReduce = 0")
        logging.warning("RoverInsight.LastAvReduce = 0")

    # Wind speed

    try:
        RoverInsight.Last_Wnd = RoverInsight.mars[RoverInsight.sol_keys_new]["HWS"]

        RoverInsight.LastWindMin = RoverInsight.Last_Wnd["mn"] * 3.6
        RoverInsight.LastWindMinReduce = round(RoverInsight.LastWindMin, 2)

        RoverInsight.LastWindMax = RoverInsight.Last_Wnd["mx"] * 3.6
        RoverInsight.LastWindMaxReduce = round(RoverInsight.LastWindMax, 2)

        RoverInsight.LastWindav = RoverInsight.Last_Wnd["av"] * 3.6
        RoverInsight.LastWindavReduce = round(RoverInsight.LastWindav, 2)
        logging.info(RoverInsight.LastWindMinReduce)
        logging.info(RoverInsight.LastWindMaxReduce)
        logging.info(RoverInsight.LastWindavReduce)
    except:
        RoverInsight.LastWindMinReduce = 0
        RoverInsight.LastWindMaxReduce = 0
        RoverInsight.LastWindavReduce = 0

        logging.warning("RoverInsight.LastWindMinReduce = 0")
        logging.warning("RoverInsight.LastWindMaxReduce = 0")
        logging.warning("RoverInsight.LastWindavReduce = 0")

    try:
        RoverInsight.Last_Wnd1 = RoverInsight.mars[RoverInsight.sol_keys_new1]["HWS"]
        logging.info(RoverInsight.Last_Wnd1)
    except:
        RoverInsight.Last_Wnd1 = 0
        logging.warning("RoverInsight.Last_Wnd1 = 0")
    try:
        RoverInsight.Last_Wnd2 = RoverInsight.mars[RoverInsight.sol_keys_new2]["HWS"]
        logging.info(RoverInsight.Last_Wnd2)
    except:
        RoverInsight.Last_Wnd2 = 0
        logging.warning("RoverInsight.Last_Wnd2 = 0")
    try:
        RoverInsight.Last_Wnd3 = RoverInsight.mars[RoverInsight.sol_keys_new3]["HWS"]
        logging.info(RoverInsight.Last_Wnd3)
    except:
        RoverInsight.Last_Wnd3 = 0
        logging.warning("RoverInsight.Last_Wnd3 = 0")
    try:
        RoverInsight.Last_Wnd4 = RoverInsight.mars[RoverInsight.sol_keys_new4]["HWS"]
        logging.info(RoverInsight.Last_Wnd4)
    except:
        RoverInsight.Last_Wnd4 = 0
        logging.warning("RoverInsight.Last_Wnd4 = 0")
    try:
        RoverInsight.Last_Wnd5 = RoverInsight.mars[RoverInsight.sol_keys_new5]["HWS"]
        logging.info(RoverInsight.Last_Wnd5)
    except:
        RoverInsight.Last_Wnd5 = 0
        logging.warning("RoverInsight.Last_Wnd5 = 0")
    try:
        RoverInsight.Last_Wnd6 = RoverInsight.mars[RoverInsight.sol_keys_new6]["HWS"]
        logging.info(RoverInsight.Last_Wnd6)
    except:
        RoverInsight.Last_Wnd6 = 0
        logging.warning("RoverInsight.Last_Wnd6 = 0")

    try:
        RoverInsight.AverageSevenDaysWind = (
            RoverInsight.Last_Wnd["av"]
            + RoverInsight.Last_Wnd1["av"]
            + RoverInsight.Last_Wnd2["av"]
            + RoverInsight.Last_Wnd3["av"]
            + RoverInsight.Last_Wnd4["av"]
            + RoverInsight.Last_Wnd5["av"]
            + RoverInsight.Last_Wnd6["av"]
        ) / 7
        RoverInsight.AverageSevenDaysWindReduce = round(
            RoverInsight.AverageSevenDaysWind, 2
        )
        logging.info(RoverInsight.AverageSevenDaysWindReduce)
    except:
        RoverInsight.AverageSevenDaysWindReduce = 0
        logging.warning("RoverInsight.AverageSevenDaysWindReduce = 0")

    # Pressure Atm
    try:
        RoverInsight.Last_Pres = RoverInsight.mars[RoverInsight.sol_keys_new]["PRE"]

        RoverInsight.LastPresMin = RoverInsight.Last_Pres["mn"]
        RoverInsight.LastPresMinReduce = round(RoverInsight.LastPresMin, 2)

        RoverInsight.LastPresMax = RoverInsight.Last_Pres["mx"]
        RoverInsight.LastPresMaxReduce = round(RoverInsight.LastPresMax, 2)

        RoverInsight.LastPresav = RoverInsight.Last_Pres["av"]
        RoverInsight.LastPresavReduce = round(RoverInsight.LastPresav, 2)
        logging.info(RoverInsight.LastPresMinReduce)
        logging.info(RoverInsight.LastPresMaxReduce)
        logging.info(RoverInsight.LastPresavReduce)
    except:
        RoverInsight.LastPresMinReduce = 0
        RoverInsight.LastPresMaxReduce = 0
        RoverInsight.LastPresavReduce = 0
        logging.warning("RoverInsight.LastPresMinReduce = 0")
        logging.warning("RoverInsight.LastPresMaxReduce = 0")
        logging.warning("RoverInsight.LastPresavReduce = 0")

    # GUI creation

    RoverInsight.welcome = "Mars InSight at Elysium Planitia latests weather report"

    RoverInsight.image = ("weatherOK.png", "insightLab.jpg")
    RoverInsight.msg = (
        (RoverInsight.welcome)
        + str("\nThe temperature is updated from Mars everyday")
        + str("\n\nLast sol for insight on Mars : ")
        + str(RoverInsight.sol_keys_new)
        + str("          ")
        + str("Minimum Wind Speed ")
        + str(RoverInsight.LastWindMinReduce)
        + str(" km/h")
        + str("\n\nLast signal date : ")
        + str(RoverInsight.last_date[:10])
        + str("               ")
        + str("Maximum Wind Speed ")
        + str(RoverInsight.LastWindMaxReduce)
        + str(" km/h")
        + str("\n\nLast signal time : ")
        + str(RoverInsight.last_date[-9:-1])
        + str(" UTC")
        + str("             ")
        + str("Average Wind Speed ")
        + str(RoverInsight.LastWindavReduce)
        + str(" km/h")
        + str("\n\nMinimum Temperature : ")
        + str(RoverInsight.LastMinReduce)
        + str(" °C")
        + str("             ")
        + str("Average 7 days Wind Speed ")
        + str(RoverInsight.AverageSevenDaysWindReduce)
        + str(" km/h")
        + str("\n\nMaximum Temperature : ")
        + str(RoverInsight.LastMaxReduce)
        + str(" °C")
        + str("             ")
        + str("Minimum Air Pressure ")
        + str(RoverInsight.LastPresMinReduce)
        + str(" Pa")
        + str("\n\nAverage Temperature : ")
        + str(RoverInsight.LastAvReduce)
        + str(" °C")
        + str("             ")
        + str("Maximum Air Pressure ")
        + str(RoverInsight.LastPresMaxReduce)
        + str(" Pa")
        + str("\n\nAverage 7 days temperature : ")
        + str(RoverInsight.AverageSevenDaysReduce)
        + str(" °C")
        + str("      ")
        + str("     Average Air Pressure ")
        + str(RoverInsight.LastPresavReduce)
        + str(" Pa")
        + str("\n\nAverage 7 days minimum temperature : ")
        + str(RoverInsight.average_seven_min_reduced)
        + str(" °C")
        + str("\n\nAverage 7 days maximum temperature : ")
        + str(RoverInsight.average_seven_max_reduced)
        + str(" °C")
        + ("\n\nCurrent season on Mars : ")
        + str((RoverInsight.ActuSeason).title())
    )
    logging.info(RoverInsight.msg)
    choices = ["Ok"]
    reply = buttonbox(RoverInsight.msg, image=RoverInsight.image, choices=choices)
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


urlData = (
    "https://mars.nasa.gov/rss/api/?feed=weather&category=insight&feedtype=json&ver=1.0"
)
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset("utf-8")
RoverInsight.mars = json.loads(data.decode(encoding))

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
