import tensorflow as tf
from models.expression_model import build_expression_model

def train_expression_model():
    """Train the facial expression recognition model."""
    model = build_expression_model()
    dataset_path = "datasets/facial_expressions/processed"

    train_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train_data = train_gen.flow_from_directory(dataset_path, target_size=(48, 48), color_mode="grayscale", class_mode="categorical", subset="training")
    val_data = train_gen.flow_from_directory(dataset_path, target_size=(48, 48), color_mode="grayscale", class_mode="categorical", subset="validation")

    model.fit(train_data, validation_data=val_data, epochs=10)
    model.save("expression_model.h5")

if __name__ == "__main__":
    train_expression_model()
