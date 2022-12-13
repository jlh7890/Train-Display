import os
import re

def loadConfig():
    data = {
        "journey": {},
        "api": {}
    }

    data["refreshTime"] = int(os.getenv("refreshTime") or 180)
    data["screenRotation"] = int(os.getenv("screenRotation") or 2)
    data["screenBlankHours"] = os.getenv("screenBlankHours") or ""
    data["dualScreen"] = bool(os.getenv("dualScreen") or False)
    data["hoursPattern"] = re.compile("^((2[0-3]|[0-1]?[0-9])-(2[0-3]|[0-1]?[0-9]))$")

    data["journey"]["departureStation"] = os.getenv("departureStation") or "LIV"
    data["journey"]["destinationStation"] = os.getenv("destinationStation") or ""
    data["journey"]["outOfHoursName"] = os.getenv("outOfHoursName") or "Aigburth"
    data["journey"]["stationAbbr"] = { "International": "Intl." }
    data["journey"]['timeOffset'] = os.getenv("timeOffset") or "0"
    data["journey"]["screen1Platform"] = os.getenv("screen1Platform") or ""
    data["journey"]["screen2Platform"] = os.getenv("screen2Platform") or ""

    data["api"]["apiKey"] = os.getenv("apiKey") or "8fe5e3f0-fe0d-4214-b927-f088286c8eb2"
    data["api"]["operatingHours"] = os.getenv("operatingHours") or "8-22"

    return data
    
