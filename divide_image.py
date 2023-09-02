import os
import cv2
import csv

folder_path = "process"
destination_path = "dataset"
file_list = os.listdir(folder_path)

csv_file = 'result/coordinates.csv'
coordinates = []

with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read and store the header row (if present)
    for row in reader:
        coordinates.append(row)

counter = 0
for i in file_list:
    image = cv2.imread(os.path.join(folder_path, i))
    for j in coordinates:
        # divided_image = image[int(coordinates[counter][1])-75:int(data[counter][1])+75,int(data[counter][0])-75:int(data[counter][0])+75]
        divided_image = image[int(j[1])-75:int(j[1])+75, int(j[0])-75:int(j[0])+75]
        filename = f"{counter}.jpg"
        counter+=1
        cv2.imwrite(os.path.join(destination_path,filename), divided_image)