# a program that downloads and saves image from web into your computer through command line argument.

import requests
import sys

url = sys.argv[1]
file_name = sys.argv[2]
res = requests.get(url)

if res.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(res.content)
        print("File downloaded! Open", file_name, "file.")
else:
    print("Invalid request!\nNot Found")
