
import sys
import os
import csv
import json
import pickle

#       0         1      2       3         4       5      6
#python reader.py in.csv out.csv 0,0,piano 3,1,mug 1,2,17 3,3,0

old_name = sys.argv[1]
if not os.path.exists(old_name):
    print(f"Input file '{old_name}' does not exist. Listing files in the directory:")
    files = os.listdir()
    for file in files:
        print(file)

new_name = sys.argv[2]


full_data =[]

if old_name.endswith(".csv"):
    with open(old_name, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            full_data.append(line)

elif old_name.endswith(".json"):
    with open(old_name, "r") as f:
        reader = json.load(f)
        
elif old_name.endswith(".pickle"):
    with open(old_name, "rb") as f:
        reader = pickle.load(f)


for value in sys.argv[3:]:

    y,x,v = value.split(",")
    y = int(y)
    x = int(x)
    full_data[x][y]= v


if new_name.endswith(".csv"):
    with open(new_name, "w" , newline="") as f:
        writer = csv.writer(f)
        for row in full_data:
            writer.writerow(row)

elif new_name.endswith(".json"):
    with open(new_name, "w" , newline="") as f:
        writer = json.dump(f)

elif new_name.endswith(".pickle"):
    with open(new_name, "wb" , newline="") as f:
        writer = pickle.dump(f)
        