import cv2
import numpy as np
# Read an image from file
image = cv2.imread('images/chessboard.jpg')

#define each coordinate of the chess board corner
upper_left = (154,25)
upper_right = (830, 25)
lower_left = (150,630)
lower_right = (834,630)

target_upper_left = (0,0)
target_upper_right = (680,0)
target_lower_left = (0,610)
target_lower_right = (680,610)


# Define the destination points (desired coordinates after transformation)
# These points define the shape to which you want to warp the rectangle
source_points = np.float32([[154, 25], [830, 25], [150, 630], [834, 630]])
destination_points = np.float32([[0, 0], [680, 0], [0, 610], [680, 610]])

# Calculate the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Perform the perspective warp
warped_image = cv2.warpPerspective(image, perspective_matrix, (680, 610))

num_rows = 8
num_cols = 9

# Calculate step sizes in both x and y directions
x_step = (target_upper_right[0] - target_upper_left[0]) / (num_cols)
y_step = (target_lower_left[1] - target_upper_left[1]) / (num_rows)

# Calculate and print coordinates for each point
intersection_list = []
for row in range(num_rows+1):
    for col in range(num_cols+1):
        x = target_upper_left[0] + col * x_step
        y = target_upper_left[1] + row * y_step
        intersection_list.append((int(x),int(y)))


markerType = cv2.MARKER_CROSS
markerSize = 15
color = (255, 0, 0)
thickness = 3
for intersection in intersection_list:
    print(intersection)
    cv2.drawMarker(warped_image, intersection, color, markerType, markerSize, thickness)

# save the image
cv2.imwrite("images/chessboard_result.jpg", warped_image)


# Display the image
cv2.imshow('Image', warped_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
