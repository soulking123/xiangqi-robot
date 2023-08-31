import cv2

# Read an image from file
image = cv2.imread('images/chessboard.jpg')

#define each coordinate of the chess board corner
upper_left = (154,25)
upper_right = (830, 25)
lower_left = (150,630)
lower_right = (834,630)

# Define color and thickness
color = (255, 0, 0)
thickness = 2

# draw the rectangle, this will represent the chess board
board_edges = (upper_left, upper_right, lower_right, lower_left)
# for i in range(4):
#     image_with_line = cv2.line(image, board_edges[i-1], board_edges[i], color, thickness)


# # define the coordinate for the line intersection, it will be 9 x 8 boxes
# horizontal_upper_line = []
# horizontal_lower_line = []
# vertical_left_line = []
# vertical_right_line = []

# horizontal_upper_length = upper_rigth[0] - upper_left[0]
# for i in range(1,9):
#     horizontal_upper_line.append(horizontal_upper_length/9*i+upper_left[0])

# horizontal_lower_length = lower_right[0] - lower_left[0]
# for i in range(1,9):
#     horizontal_lower_line.append(horizontal_lower_length/9*i+lower_left[0])

# vertical_left_length = lower_left[1] - upper_left[1]
# print("asa",vertical_left_length)
# for i in range(1,8):
#     vertical_left_line.append(vertical_left_length/8*i+upper_left[1])

# print(vertical_left_line)

num_rows = 8
num_cols = 9

# Calculate step sizes in both x and y directions
x_step = (upper_right[0] - upper_left[0]) / (num_cols)
y_step = (lower_left[1] - upper_left[1]) / (num_rows)

# Calculate and print coordinates for each point
for row in range(num_rows+1):
    for col in range(num_cols+1):
        x = upper_left[0] + col * x_step
        y = upper_left[1] + row * y_step
        print(f"Point ({x}, {y})")





# Display the image
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
