# Imports
from datetime import datetime
from statistics import mean
import numpy as np

# Get 3 readings from the user
readings = list()
print("Please enter readings in format: upper/lower/pulse")
for i in range(2):
    reading = input("Enter reading "+str(i+1)+": ")
    readings.append(reading)

# Separate corresponding readings
upper = list()
lower = list()
pulse = list()
for reading in readings:
    up, lw, pul = reading.split("/")
    upper.append(int(up))
    lower.append(int(lw))
    pulse.append(int(pul))

# Compute Averages and round
avg_lower = round(mean(lower))
avg_upper = round(mean(upper))
avg_pulse = round(mean(pulse))

# File Handeling
with open("record.csv", "a+") as file_object:
    current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file_object.write(
        f"{current_datetime}, {avg_upper}, {avg_lower}, {avg_pulse}" + "\n")
