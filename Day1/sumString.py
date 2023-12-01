import argparse
import re

intmap = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine":"9"
}

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help = "Calibrations File")

args = parser.parse_args()

file = open('calibration/' + args.file, 'r')
Lines = file.readlines()

sum = 0

for line in Lines:
    search = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))",line)
    if len(str(search[0])) > 1:
        search[0] = intmap[search[0]]
    if len(str(search[-1])) > 1:
        search[-1] = intmap[search[-1]]
    combine = str(search[0]) + str(search[-1])
    sum = sum + int(combine)

print("The Total Calibration is " + str(sum))

#between 54270 and 54718