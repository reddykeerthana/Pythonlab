
import os

filename = os.path.join(os.path.dirname(__file__), "log.txt")

try:
    with open(filename, "r") as file:
        print("----- Log File Contents -----")

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Log file not found!")
