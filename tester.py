import requests
import os
from pathlib import Path

def test_download_endpoint():
    url = 'https://nrc-t3.onrender.com/download'  # Update the URL according to your deployment
    response = requests.get(url)
    if response.status_code == 200:
        download_folder = str(Path.home() / "Downloads")
        file_path = os.path.join(download_folder, "downloaded_file.csv")
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return {"status": "success", "message": "File downloaded successfully."}
    else:
        return {"status": "failure", "message": "Failed to download file."}

if __name__ == '__main__':
    print(test_download_endpoint())
