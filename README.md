# ICU Patient Monitoring System

## Overview

The ICU Patient Monitoring System uses computer vision and deep learning to analyze patients' activities and facial expressions in real-time. The system identifies patient discomfort or irregular activities to provide insights for medical staff, improving patient care and safety in Intensive Care Units (ICUs).

## Features

- **Activity Recognition**: Identifies patient movements such as walking, sitting, or lying down.
- **Facial Expression Analysis**: Detects discomfort or distress from facial expressions.
- **Real-time Processing**: Analyzes live video streams from cameras installed in ICUs.
- **Alert System**: Sends alerts when irregular activities or discomfort are detected.

## File Directory Structure

```
ICU_patient_monitoring/
├── data/
│   ├── raw_data/                # Raw datasets downloaded from Kaggle
│   ├── preprocessed_data/       # Preprocessed data for training
├── models/
│   ├── activity_model.h5        # Trained activity recognition model
│   ├── facial_expression_model.h5 # Trained facial expression recognition model
├── notebooks/
│   ├── activity_training.ipynb  # Jupyter notebook for activity model training
│   ├── expression_training.ipynb # Jupyter notebook for facial expression model training
├── src/
│   ├── activity_recognition.py  # Code for activity recognition
│   ├── facial_expression.py     # Code for facial expression analysis
│   ├── main.py                  # Main script for real-time monitoring
├── utils/
│   ├── data_preprocessing.py    # Data preprocessing functions
│   ├── helper.py                # Helper functions
├── requirements.txt             # Python dependencies
├── README.md                    # Project description and setup guide
```

## Dataset

### Activity Recognition Dataset
- **Source**: [Kaggle - Real-life Human Activity Dataset](https://www.kaggle.com/)
- Includes multiple activity labels such as walking, sitting, and lying down.

### Facial Expression Dataset
- **Source**: [Kaggle - FER2013 Dataset](https://www.kaggle.com/)
- Contains facial expression labels such as happy, sad, angry, and neutral.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8+
- Virtualenv
- TensorFlow 2.x
- OpenCV
- NumPy
- Pandas
- Matplotlib

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/nareshAiNexus/ICU_patient_monitoring.git
cd ICU_patient_monitoring
```

### Step 2: Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Download Datasets

1. Download the activity recognition and facial expression datasets from Kaggle.
2. Place the datasets in the `data/raw_data/` directory.
3. Run the preprocessing script to prepare the data for training:

```bash
python utils/data_preprocessing.py
```

### Step 4: Train the Models

Use the Jupyter notebooks provided in the `notebooks/` directory to train the models:

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open `activity_training.ipynb` to train the activity recognition model.
3. Open `expression_training.ipynb` to train the facial expression model.

The trained models will be saved in the `models/` directory.

### Step 5: Run the Monitoring System

Use the `main.py` script to start real-time monitoring:

```bash
python src/main.py
```

## How to Use

1. Connect the camera feed to the system.
2. Run the monitoring system.
3. Alerts will be displayed on the console or sent to a designated notification system.

## Project Workflow

1. **Data Collection**: Collect and preprocess activity and facial expression datasets.
2. **Model Training**: Train deep learning models for activity recognition and facial expression analysis.
3. **Real-Time Monitoring**: Integrate models with camera feed for real-time analysis.
4. **Alert System**: Generate alerts for irregular activities or discomfort.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
