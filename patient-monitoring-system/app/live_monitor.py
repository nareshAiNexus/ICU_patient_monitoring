import cv2
from utils.inference import process_frame

def monitor_live_feed():
    """Function to monitor live feed from the camera."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Process the frame
        result = process_frame(frame)

        # Display the processed frame
        cv2.imshow("Live Monitoring", result)

        # Break loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    monitor_live_feed()
