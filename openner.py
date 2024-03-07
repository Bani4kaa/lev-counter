import cv2

def main():
    # Get the list of connected cameras
    num_cameras = 0
    for index in range(10):
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        num_cameras += 1
        cap.release()

    if num_cameras == 0:
        print("No cameras found.")
        return

    print(f"Found {num_cameras} camera(s).")

    # Prompt the user to select a camera
    while True:
        try:
            camera_index = int(input(f"Enter camera index (0-{num_cameras-1}): "))
            if 0 <= camera_index < num_cameras:
                break
            else:
                print("Invalid camera index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Open the selected camera
    cap = cv2.VideoCapture(camera_index)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        # Display the frame
        cv2.imshow('Camera', frame)

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()