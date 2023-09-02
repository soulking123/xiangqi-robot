import cv2

# Initialize the camera
cap = cv2.VideoCapture(2)  # 0 represents the default camera (you can change this to another index if you have multiple cameras)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# x 640
# y 480
# Set the frame size to 1920x1080 (1080p)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

num=0
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    k = cv2.waitKey(5)

    # Check if the frame was read successfully
    if k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('process/img' + str(num) + '.jpg', frame)
        print("image saved!")
        num += 1
    elif k == ord("q"):
        break

    frame = cv2.line(frame, (0,360), (1280,360), (255,0,0), 1)
    frame = cv2.line(frame, (640,0), (640,720), (255,0,0), 1)

    # Display the frame
    cv2.imshow('Camera Stream', frame)


    # Press 'q' to exit the loop and close the window
    

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

