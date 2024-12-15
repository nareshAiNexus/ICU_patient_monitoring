import cv2

def preprocess_frame(frame, target_size=(48, 48)):
    """Preprocess a frame for facial expression model."""
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray_frame, target_size)
    normalized_frame = resized_frame / 255.0
    return normalized_frame.reshape(1, target_size[0], target_size[1], 1)
