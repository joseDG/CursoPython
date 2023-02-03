sentence = "What is the Airspeed Velocity of an Unlanden Swallow"

result = {word:len(word) for word in sentence.split()}

print(result)

wather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wenesday": 15,
    "Thruesday": 16,
    "Friday": 17,
    "Sunday": 18,
}

weather_f = {day:(temp_c*9/5) + 32 for (day, temp_c) in wather_c.items()}

print(weather_f)