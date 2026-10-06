cleaned_report = []

with open("metars.txt") as file:
    for item in file:
        clean_up = item.strip().split()
        try:
            # Wind Speed and Direction Split
            wind_dir = int(clean_up[2][0:3])
            wind_spd = int(clean_up[2][3:5])
            # Temperature Celsius and Dew Point Split
            temp_c = clean_up[-2].split("/")[0]
            if "M" in temp_c:
                temp_c = clean_up[-2].split("/")[0][1:3]
                temp_c = int(temp_c) * -1
            else:
                temp_c = int(temp_c)
            # The Dictionary
            report_template = {"origin": clean_up[0], 
                               "time": clean_up[1], 
                               "wind": clean_up[2], 
                               "visibility": clean_up[3], 
                               "sky_and_weather": clean_up[4:-2], 
                               "altimeter": clean_up[-1], 
                               "temperature": clean_up[-2],
                               "wind_direction": wind_dir,
                               "wind_speed": wind_spd,
                               "temperature_C": temp_c }
            cleaned_report.append(report_template)
        except (ValueError, IndexError):
            print(f"Mistake on METAR report: {item.strip()}")
        
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

average_temperature = total_temperature / len(cleaned_report)
print("\n --AVERAGE TEMPERATURE--")
print(f"{average_temperature} degrees Celsius.")

print("\n--PROGRAM COMPLETE--")