import cv2
import csv

csv_file = 'result/coordinates.csv'  # Replace with your CSV file path

# Initialize a list to store the data
data = []
counter = 0

# Read the CSV file and store its contents in the 'data' list
with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read and store the header row (if present)
    for row in reader:
        data.append(row)
print(data)

def mouse_callback(event, x, y, flags, param):
    global image,counter
    

    if event == cv2.EVENT_LBUTTONDOWN:
        # print(int(data[counter][0])-75,int(data[counter][0])+75,int(data[counter][1])-75,int(data[counter][1])+75)
        try:
            images = image[int(data[counter][1])-75:int(data[counter][1])+75,int(data[counter][0])-75:int(data[counter][0])+75]
        except:
            cv2.destroyAllWindows()
        counter += 1
        # print(images.shape)
        cv2.imshow('Image', images)



image = cv2.imread("process/img1.jpg")

cv2.namedWindow('Image')
cv2.imshow('Image', image)
cv2.setMouseCallback('Image', mouse_callback)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
