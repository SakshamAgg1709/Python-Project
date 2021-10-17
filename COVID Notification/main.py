from plyer import notification
import requests
from bs4 import BeautifulSoup
def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\\Python Projects\\COVID Notification\\icon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    notify("Saksham", "Let's stop this spread of COVID-19 together")
    # myHtmldata = getData("https://www.mohfw.gov.in/")
    # # print(myHtmldata)
    # soup = BeautifulSoup(myHtmldata, 'html.parser')
    # # print(soup.prettify())
    # myDataStr = ""
    # #1st table is not of our use so we use tbody[1]
    # for tr in soup.findAll('tbody').__format__('tr'):
    #     myDataStr = tr.get_text()
    # print(myDataStr)
