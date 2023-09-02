import os
import csv

csv_file = 'coordinates.csv'
coordinates = []
with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read and store the header row (if present)
    for row in reader:
        coordinates.append(row)

list1 = ["hitam benteng", "hitam kuda", "hitam gajah", "hitam mentri", "hitam raja", "hitam cannon", "hitam prajurit", 
        "merah benteng", "merah kuda", "merah gajah", "merah mentri", "merah raja", "merah cannon", "merah prajurit", "empty"]

print(len(os.listdir("dataset")))