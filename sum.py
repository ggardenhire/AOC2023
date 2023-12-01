import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help = "Calibrations File")

args = parser.parse_args()

file = open('calibration/' + args.file, 'r')
Lines = file.readlines()

sum = 0

for line in Lines:
    search = re.findall(r"\d",line)
    combine = str(search[0]) + str(search[-1])
    print(combine)
    sum = sum + int(combine)

print("The Total Calibration is " + str(sum))