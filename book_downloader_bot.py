# a web robot that downloads a book from a particular website and shows the downloaded book in the browser.

import requests
import sys
import os
import webbrowser as wb

formData = {"name": "Rashed Rahat",
            "email": "imrashedrahat@gmail.com", "country": "Bangladesh"}
baseUrl = "http://subeen.com/download/"
url = baseUrl + "process.php"
res = requests.post(url, data=formData)

if res.ok is False:
    sys.exit("Error downloading the file!")

with open("cpbook.pdf", "wb") as fp:
    fp.write(res.content)

print("Book download complete!\nOpening the file in browser..")

filePath = os.path.realpath("cpbook.pdf")
wb.open("file://" + filePath)
