import os
import kaggle
import zipfile

def download_dataset(dataset_name, download_path, extract_to):
    """
    Downloads and extracts a Kaggle dataset.
    
    Args:
        dataset_name (str): The Kaggle dataset identifier (e.g., 'dansbecker/fer2013').
        download_path (str): Path to save the downloaded dataset.
        extract_to (str): Path to extract the dataset.
    """
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    print(f"Downloading {dataset_name}...")
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)

    # Extract the dataset if it's a zip file
    for file in os.listdir(download_path):
        if file.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(download_path, file), "r") as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"Extracted {file} to {extract_to}")
    
    print(f"Dataset {dataset_name} downloaded and extracted.")

if __name__ == "__main__":
    datasets = {
        "facial_expressions": "ashishpatel26/facial-expression-recognitionferchallenge",
        "human_activities": "sushilrajtilak/human-activity-recognition"
    }
    for name, kaggle_id in datasets.items():
        download_dataset(kaggle_id, f"datasets/{name}/raw", f"datasets/{name}/processed")
