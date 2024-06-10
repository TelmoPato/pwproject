import requests
import zipfile
import os

def download_and_extract_icons(url, extract_to):
    response = requests.get(url)
    zip_path = os.path.join(extract_to, 'icons.zip')
    with open(zip_path, 'wb') as file:
        file.write(response.content)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)

download_and_extract_icons('URL_DO_ZIP_ICONS', 'static/meteo/icons')