import csv

with open('updated_dataset.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

dif = 0 # this is the abstract labour of dif between theoretical and actual price (it might be neg that will be a problem)
count = 0
for row in data[1:]:
    dif += float(row[2]) - float(row[3])
    count += 1

print(dif/count) 
# 23.125913978494623