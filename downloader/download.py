# Author: Muhammad Buhari
# GitHub: github.com/al-mohad
# Program: DOWNLOAD FILE

import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


download("http://download.wallpaperseveryday.com/getimage.php?id=96536&name=Were%20chikens%20also%20blue,%20pink%20and%20yellow?")
# To be continue...
