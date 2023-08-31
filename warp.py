import cv2
import numpy as np
# Read an image from file
image = cv2.imread('images/chessboard.jpg')

#define each coordinate of the chess board corner
upper_left = (154,25)
upper_right = (830, 25)
lower_left = (150,630)
lower_right = (834,630)

# Define the destination points (desired coordinates after transformation)
# These points define the shape to which you want to warp the rectangle
source_points = np.float32([[154, 25], [830, 25], [150, 630], [834, 630]])
destination_points = np.float32([[0, 0], [680, 0], [0, 610], [680, 610]])

# Calculate the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Perform the perspective warp
warped_image = cv2.warpPerspective(image, perspective_matrix, (680, 610))

markerType = cv2.MARKER_CROSS
markerSize = 15
color = (255, 0, 0)
thickness = 3
cv2.drawMarker(warped_image, (200, 100), color, markerType, markerSize, thickness)
cv2.drawMarker(warped_image, (100, 100), color, markerType, markerSize, thickness)


# draw the rectangle, this will represent the chess board
board_edges = (upper_left, upper_right, lower_right, lower_left)
# for i in range(4):
#     image_with_line = cv2.line(image, board_edges[i-1], board_edges[i], color, thickness)




# Display the image
cv2.imshow('Image', warped_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
