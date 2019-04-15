# a program that saves a web page into a file and opens the file.

import requests
import os
import webbrowser as wb

url = "https://rashedrahat.github.io/imRAR"
res = requests.get(url)

with open("ProfileOfRashedRahat.html", "w", encoding = res.encoding) as f:
    f.write(res.text)

file_path = os.path.realpath("ProfileOfRashedRahat.html")
wb.open("file://" + file_path)
