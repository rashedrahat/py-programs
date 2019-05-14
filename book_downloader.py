# a program that downloads a book from the internet and saves into your computer.

import requests
import sys

base_url = "http://subeen.com/download/"
info_data = {"name": "Rashed",
             "email": "rashedrahat@outlook.com", "country": "Bangladesh"}
url = base_url + "process.php"
res = requests.post(url, data=info_data)

if res.ok is False:
    sys.exit("Error downloading the file!")

with open("cpbook.pdf", "wb") as f:
    f.write(res.content)

print("Book download complete!")
