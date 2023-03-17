import smtplib
import os
from bs4 import BeautifulSoup

# environment variables for safety
email_addr = os.environ.get("STARI_DEV_EMAIL_ADDR")
email_pass = os.environ.get("STARI_DEV_EMAIL_PASS")
email_to = os.environ.get("STARI_DEV_EMAIL_ADDR2")


def htmlTrimmer(string):
    soup = BeautifulSoup(string, features="lxml")

    soup.prettify()
    for scriptTag in soup.select("script"):
        scriptTag.extract()

    for metaTag in soup.select("meta"):
        metaTag.extract()

    return str(soup).replace('\r', '')

# get the title of the website


def extractTitle(string):
    soup = BeautifulSoup(string, features="lxml")
    return soup.title.string

# send email using gmail SMTP


def sendMail(emailSubject, email_addr, email_to, email_pass, url):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        # encrypt the connection
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        # login to email
        smtp.login(email_addr, email_pass)

        # construct the email
        subject = "Up! " + emailSubject
        body = "The startlist has been uploaded / updated. Check the website: " + url
        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(email_addr, email_to, msg)


def websiteCheck(url, response):
    print("Checking website... " + url)

    # create file if it does not exist
    if os.path.exists("lastCheck.html") == False:
        open("lastCheck.html", 'w+', encoding='utf-8').close()

    # otherwise just open it
    f = open("lastCheck.html", 'r', encoding='utf-8')
    lastHtml = f.read()
    f.close()

    #trim the HTML using the function created above and extract the title
    trimmedHtml = htmlTrimmer(response.text)
    title = extractTitle(trimmedHtml).encode(
        'utf-8').decode('ascii', 'ignore') # remove non-ascii characters

    #check for changes and send email if there are any
    if trimmedHtml == lastHtml:
        return False

    else:
        file = open("lastCheck.html", 'w', encoding='utf-8')
        file.write(trimmedHtml)
        file.close()
        sendMail(title, email_addr, email_to, email_pass, url)
        return True
