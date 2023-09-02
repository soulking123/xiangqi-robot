import cv2
import numpy as np

# Read the image
image = cv2.imread('process/img0.jpg')  # Replace 'your_image.jpg' with your image file path

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection (optional)
edges = cv2.Canny(gray, threshold1=50, threshold2=150, apertureSize=3)

# Detect lines using Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

# Check if lines were detected
if lines is not None and len(lines) >= 2:
    # Calculate the intersection point of the first two detected lines
    rho1, theta1 = lines[0, 0]
    rho2, theta2 = lines[1, 0]
    A = np.array([
        [np.cos(theta1), np.sin(theta1)],
        [np.cos(theta2), np.sin(theta2)]
    ])
    b = np.array([[rho1], [rho2]])
    intersection = np.linalg.solve(A, b)
    intersection = (int(intersection[0][0]), int(intersection[1][0]))  # Convert to integers

    # Draw the lines
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    print("===========")
    print(intersection)

    # Draw the intersection point on the image
    cv2.circle(image, intersection, 5, (0, 255, 0), -1)

    # Display the image with lines and intersection point
    cv2.imshow('Image with Lines and Intersection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No or not enough lines detected in the image.")
