import csv
from collections import Counter

with open("WeightHeight.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

height = []

for i in range(len(fileData)):
    num = fileData[i][1]
    height.append(float(num))

data = Counter(height)

# print(data)

mode_data_for_range = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height,occurence in data.items():
    if(50 < float(height) <60):
        mode_data_for_range["50-60"] += occurence
    elif(60 < float(height) <70):
        mode_data_for_range["60-70"] += occurence
    elif(70< float(height) <80):
        mode_data_for_range["70-80"] += occurence
        
# print(mode_data_for_range)

mode_range, mode_occurence = 0, 0

for range,occurence in mode_data_for_range.items():
    if(occurence > mode_occurence):
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1])/2)

print("Mode is " + str(mode))
