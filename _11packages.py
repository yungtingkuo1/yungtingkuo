import sys
print(sys.argv)

new_name = sys.argv[0]
if not os.path.exists("customers.csv"):
    print("Input file 'customers.csv' does not exist. Listing files in the directory:")

import os
new_name = input("Type in the new name for the .csv file:")
os.rename ("customers.csv", new_name)

with open("customers.csv", "r") as f:
    for line in f:
        print(line.strip().split(","))

import csv

full_data =[]

with open("customers.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        full_data.append(line)

for idx, row in enumerate(full_data):
    print(row)

with open("customers_edit.csv", "w" , newline="") as f:
    writer = csv.writer(f)
    for row in full_data:
        writer.writerow(row)