
import sys
import os
import csv
import json
import pickle

#       0         1      2       3         4       5      6
#python reader.py in.csv out.csv 0,0,piano 3,1,mug 1,2,17 3,3,0

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        raise NotImplementedError

class CSVFileReader(FileReader):
    def read_data(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            full_data = [line for line in reader]
        return full_data

class JSONFileReader(FileReader):
    def read_data(self):
        with open(self.filename, 'r') as f:
            full_data = json.load(f)
        return full_data

class PickleFileReader(FileReader):
    def read_data(self):
        with open(self.filename, 'rb') as f:
            full_data = pickle.load(f)
        return full_data

class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        raise NotImplementedError

class CSVFileWriter(FileWriter):
    def write_data(self, data):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)

class JSONFileWriter(FileWriter):
    def write_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)

class PickleFileWriter(FileWriter):
    def write_data(self, data):
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)

class DataModifier:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def modify_data(self, values):
        data = self.reader.read_data()
        for value in values:
            y, x, v = value.split(',')
            y = int(y)
            x = int(x)
            data[x][y] = v
        self.writer.write_data(data)

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
        