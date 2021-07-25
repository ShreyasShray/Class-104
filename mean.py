import csv

with open("WeightHeight.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

height = []

for i in range(len(fileData)):
    num = fileData[i][1]
    height.append(float(num))

n = len(height)
total = 0

for x in height:
    total += x

mean = total/n

print("Mean is ", str(mean))