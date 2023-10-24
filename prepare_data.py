import os
import requests
import hashlib
import zipfile

# URLs for the datasets
adult_zip_url = "https://archive.ics.uci.edu/static/public/2/adult.zip"
adult_csv_url = "https://raw.githubusercontent.com/socialfoundations/folktables/main/adult_reconstruction.csv"

# File paths for downloaded data and files
data_dir = "data"
zip_file_path = os.path.join(data_dir, "adult.zip")
csv_file_path = os.path.join(data_dir, "folktables", "adult_reconstruction.csv")
zip_hash_file = os.path.join(data_dir, "adult_zip_hash.txt")
csv_hash_file = os.path.join(data_dir, "adult_csv_hash.txt")

def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        exit(1)

def compute_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def main():
    os.makedirs(data_dir, exist_ok=True)
    # Download the ZIP file
    if not os.path.isfile(zip_file_path):
        download_file(adult_zip_url, zip_file_path)

    # Verify the ZIP file's integrity
    zip_hash = compute_hash(zip_file_path)
    with open(zip_hash_file, "w") as f:
        f.write(zip_hash)

    # Unzip the file
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(data_dir)

    # Download the CSV file
    if not os.path.isfile(csv_file_path):
        download_file(adult_csv_url, csv_file_path)

    # Verify the CSV file's integrity
    csv_hash = compute_hash(csv_file_path)
    with open(csv_hash_file, "w") as f:
        f.write(csv_hash)

    print("Data downloaded and verified successfully.")
