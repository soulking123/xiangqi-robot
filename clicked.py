import cv2
import numpy as np
import csv

# Define a list to store dot coordinates and their labels
dots = []
dot_labels = []

# Counter for labeling the dots
dot_counter = 1

# Define a callback function to handle mouse events
def mouse_callback(event, x, y, flags, param):
    global dots, overlay_image, dot_counter
    

    if event == cv2.EVENT_LBUTTONDOWN:
        print("asad")
        dots.append((x, y))  # Add a dot at the click position
        dot_labels.append(dot_counter)  # Add a label for the dot
        dot_counter += 1
        draw_dots()

    elif event == cv2.EVENT_RBUTTONDOWN:
        if dots:
            dots.pop()  # Remove the last added dot
            dot_counter -= 1
            dot_labels.pop()  # Remove the label for the dot
            draw_dots()

# Function to draw all dots on the overlay image
def draw_dots():
    global overlay_image

    # Create a copy of the original image to draw dots on
    overlay_image = np.copy(image)

    for dot, label in zip(dots, dot_labels):
        cv2.circle(overlay_image, dot, 5, (0, 0, 255), -1)  # Draw the dot in red
        cv2.putText(overlay_image, str(label), (dot[0] + 10, dot[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Add the label

    # Combine the overlay image with the original image using alpha blending
    alpha = 0.7  # Adjust the transparency of the dots

    cv2.imshow('Mouse Click Example', overlay_image)

# Read the image
image = cv2.imread('process/img0.jpg')  # Replace 'your_image.jpg' with your image file path

# Create an overlay image with the same dimensions as the original image
overlay_image = np.copy(image)

# Set the window name and display the image
cv2.namedWindow('Mouse Click Example')
cv2.imshow('Mouse Click Example', image)

# Set the mouse callback function for the window
cv2.setMouseCallback('Mouse Click Example', mouse_callback)

# Wait for the user to click the mouse or press any key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()


csv_file = 'coordinates.csv'

# Open the CSV file in write mode and write the coordinates
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['X', 'Y'])  # Write header row
    writer.writerows(dots)

print(f"Coordinates saved to {csv_file}.")
