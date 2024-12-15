import cv2
from models.expression_model import build_expression_model
from utils.preprocess import preprocess_frame

expression_model = build_expression_model()
expression_model.load_weights("path_to_expression_model_weights.h5")

def process_frame(frame):
    """Process the frame to detect patient expressions."""
    preprocessed_frame = preprocess_frame(frame)
    predictions = expression_model.predict(preprocessed_frame)
    expression = predictions.argmax()
    return frame  # You can overlay prediction results on the frame
