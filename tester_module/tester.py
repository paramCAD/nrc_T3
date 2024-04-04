import requests

def test_download_endpoint():
    url = 'https://nrc-t3.onrender.com/download' 
    response = requests.get(url)
    if response.status_code == 200:
        with open('downloaded_file.csv', 'wb') as f:
            f.write(response.content)
        return {"status": "success", "message": "File downloaded successfully."}
    else:
        return {"status": "failure", "message": "Failed to download file."}

if __name__ == '__main__':
    result = test_download_endpoint()
    print(result['message'])
