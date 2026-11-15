def get_temp(temp_token):
    temp_dictionary = {"temperature": None, "dew_point": None}
    temperature_split = temp_token.split("/")
    if "M" in temperature_split[0]:
        temperature = int(temp_token[1:3]) * -1
    else:
        temperature = int(temp_token[0:2])
    dew_point = temperature_split[1]
    if dew_point == "":
        dew_point = None
    elif "M" in temperature_split[1]:
        dew_point = int(temp_token[5:7]) * -1
    else:
        dew_point = int(temp_token[4:6])
    temp_dictionary["temperature"] = temperature
    temp_dictionary["dew_point"] = dew_point
    return temp_dictionary

def get_wind(wind_token):
    if "VRB" in wind_token:
        wind_direction = None
    else:
        wind_direction = int(wind_token[0:3])
    if "G" in wind_token:
        wind_gust = int(wind_token[6:8])
    else:
        wind_gust = None
    wind_speed = int(wind_token[3:5])
    wind_dictionary = {"direction": wind_direction, "speed": wind_speed, "gust": wind_gust}
    return wind_dictionary

def get_weather(sky_wxr_token):
    weather_condition_list = []
    sky_condition_list = []
    for token in sky_wxr_token:
        if token.startswith(("FEW", "SCT", "BKN", "OVC", "VV")):
            sky_condition_list.append(token)
        else:
            weather_condition_list.append(token)
    wxr_and_sky_dictionary = {"weather": weather_condition_list, "sky": sky_condition_list}
    return wxr_and_sky_dictionary 


def get_visibility(visibility_token):
    if visibility_token == "CAVOK":
        visibility_dictionary = {"visibility": "CAVOK"}
    else:
        visibility_dictionary = {"visibility": visibility_token}
    return visibility_dictionary


def parse_metar(raw_metar):
    # Declaring Variables
    visibility_token = None
    station = None
    time = None
    wind_token = None
    sky_wxr_token = []
    temp_token = None
    rvr_token = None
    altimeter = None
    cloud_prefixes = ("FEW","SCT","BKN","OVC","VV")

    clean_up = raw_metar.strip().split()
    # For Loop Parsing by Category
    for token in clean_up:
        if len(token) == 4:
            if  token == "AUTO":
                continue
            if token.isdigit():
                visibility_token = token
            elif station != None:
                sky_wxr_token.append(token)
            else:
                station = token
        elif token.endswith("Z") :
            time = token
        elif token.endswith("KT"):
            wind_token = token
        elif token.startswith(cloud_prefixes):
            sky_wxr_token.append(token)
        elif token.startswith("R") and "/" in token:
            rvr_token = token
        elif "/" in token:
            temp_token = token
        elif token.startswith("Q") or token.startswith("A"):
            altimeter = token
        elif token == "RMK":
            break
        else:
            if token == "METAR":
                continue
            elif token == "CAVOK":
                visibility_token = token
            elif station != None:
                sky_wxr_token.append(token)



    # Call Ups
    wind = get_wind(wind_token)
    visibility = get_visibility(visibility_token)
    sky_weather = get_weather(sky_wxr_token)
    temperature = get_temp(temp_token)

    metar_dictionary = {"origin": station, 
                        "time": time, 
                        "wind_speed": wind["speed"], 
                        "wind_direction": wind["direction"], 
                        "wind_gust": wind["gust"],
                        "visibility": visibility["visibility"],
                        "weather": sky_weather["weather"],
                        "clouds": sky_weather["sky"],
                        "temperature_C": temperature["temperature"],
                        "dew_point": temperature["dew_point"],
                        "altimeter": altimeter}
    return metar_dictionary

cleaned_report = []

with open("metars.txt") as file:
    for raw_metar in file:
        try:
            cleaned_report.append(parse_metar(raw_metar))
        except (ValueError, IndexError, TypeError):
            print(f"Mistake on METAR report: {raw_metar.strip()}")
        
#Full Report
print(cleaned_report)

#Wind Speeds
print("\n --STATIONS ABOVE 10KTS--")

for report in cleaned_report:
    if report["wind_speed"] > 10:
        print(report["origin"])

# Temperature Average
total_temperature = 0
for report in cleaned_report:
    total_temperature += report["temperature_C"]

if len(cleaned_report) != 0:
    average_temperature = total_temperature / len(cleaned_report)
    print("\n --AVERAGE TEMPERATURE--")
    print(f"{average_temperature:.1f} degrees Celsius.")
else:
    print("No data available!")

print("\n--PROGRAM COMPLETE--")

