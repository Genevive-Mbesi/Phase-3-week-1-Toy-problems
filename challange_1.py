def convert_12_hour_to_24_hour(hour,minute,period):
    if minute < 10:
        minute = f"0{str(minute)}"

    if period == "am":
        if hour < 10:
            hour = f"0{str(hour)}"
        time = f"{str(hour)}{str(minute)}"
        return time
    else:
        if hour == 12:
            hour = "00"
        else:
            hour = hour + 12
        time = f"{str(hour)}{minute}"
        return time

print (convert_12_hour_to_24_hour(8,30,'am'))
print (convert_12_hour_to_24_hour(8,30,'pm'))
print (convert_12_hour_to_24_hour(9,9,'am'))