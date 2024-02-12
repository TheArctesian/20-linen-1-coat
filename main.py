import csv

factor = 1375 / 186

with open('data/data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

data[0].append('TheoreticalLinen')

for row in data[1:]:  
    original_price = float(row[1]) 
    adjusted_price = original_price * factor
    row.append(adjusted_price)  

with open('updated_dataset.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Updated dataset with AdjustedPriceLinen has been saved to updated_dataset.csv")
