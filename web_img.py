# a program that downloads and saves image from web into your computer.

import requests
url = "https://avatars1.githubusercontent.com/u/37572137?s=460&v=4"
res = requests.get(url)
if res.status_code == 200:
    with open("RashedRahat.png", "wb") as f:
        f.write(res.content)
        print("File downloaded! Open 'RashedRahat.png' file.")
else:
    print("Invalid request!\nNot Found")
