import requests
import os

import functions

# url to check, it can be changed to any websites url
url = "https://triathlon.org/events/start_list/2023_world_triathlon_aquathlon_championships_ibiza/584002"

# environment variables for safety
email_addr = os.environ.get("STARI_DEV_EMAIL_ADDR")
email_pass = os.environ.get("STARI_DEV_EMAIL_PASS")
email_to = os.environ.get("STARI_DEV_EMAIL_ADDR2")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
           "Pragma": "no-cache", "Cache-Control": "no-cache"}

response = requests.get(url, headers=headers)

# create a new txt file if it doesn't exist already
if os.path.exists("lastCheck.html") == False:
    open("lastCheck.html", 'w+', encoding='utf-8').close()

f = open("lastCheck.html", 'r', encoding='utf-8')
lastHtml = f.read()
f.close()

# trim the html using htmlTrim()
trimmedHtml = functions.htmlTrimmer(response.text)
title = functions.extractTitle(trimmedHtml).encode('utf-8').decode('ascii', 'ignore')

# check if the html is changed or not
# for the first time it will always be changed
if trimmedHtml == lastHtml:
    print("Website did not change!")

else:
    file = open("lastCheck.html", 'w', encoding='utf-8')
    file.write(trimmedHtml)
    file.close()
    functions.sendMail(title, email_addr, email_to, email_pass, url)
    print("Website Changed! Email sent!")
