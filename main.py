from datetime import datetime
from statistics import mean
import numpy as np

avg_upper = int(input("Enter Sys: "))
avg_lower = int(input("Enter Dia: "))
avg_pulse = int(input("Enter Pulse: "))

# File Handeling
with open("record.csv", "a+") as file_object:
    current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file_object.write(
        f"{current_datetime},{avg_upper},{avg_lower},{avg_pulse}" + "\n")
