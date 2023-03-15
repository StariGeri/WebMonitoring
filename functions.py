import smtplib
from bs4 import BeautifulSoup


def htmlTrimmer(string):
    soup = BeautifulSoup(string, features="lxml")

    soup.prettify()
    for scriptTag in soup.select("script"):
        scriptTag.extract()

    for metaTag in soup.select("meta"):
        metaTag.extract()

    return str(soup).replace('\r', '')

#get the title of the website
def extractTitle(string):
    soup = BeautifulSoup(string, features="lxml")
    return soup.title.string

# send email using gmail SMTP
def sendMail(emailSubject, email_addr,email_to, email_pass, url):
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
