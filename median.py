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

sortedData = height.sort()

if(n % 2 == 0):
    median1 = float(height[n//2])
    median2 = float(height[n//2-1])
    median = (median1 + median2)/2
else:
    median = float(height[n//2])

print(n)
print("Median is " + str(median))