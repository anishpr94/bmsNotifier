import urllib2
from bs4 import BeautifulSoup
import time

import smtplib

book_my_show_url = "https://in.bookmyshow.com/buytickets/avengers-infinity-war-kochi/movie-koch-ET00053419-MT/20180430"
gmailaddress = 'mymail@gmail.com'
gmailpassword = 'password'
mailto = 'toAddress@gmail.com'

while True:
    requester = urllib2.Request(book_my_show_url, headers={'User-Agent': "Magic Browser"})
    connector = urllib2.urlopen(requester)
    connector_reader = connector.read()
    soup = BeautifulSoup(connector_reader, "html.parser")
    available = False
    msg = 'Not Yet'
    text = soup.get_text()
    for ultag in soup.find_all('ul', {'id': 'venuelist'}):
        for litag in ultag.find_all('li', {'class': 'list'}):
            if "Cinemax: Oberon, Kochi" in litag.text or "Q Cinemas: Gold Souk Grande" in litag.text:
                if "Cinemax: Oberon, Kochi" in litag.text:
                    msg = "Available_Cinemax_Oberon,Kochi"
                    available = True
                if "Q Cinemas: Gold Souk Grande" in litag.text:
                    msg += "\nAvailable_QCinemas_GoldSouk_Grande"
                    available = True           
    if available:
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(gmailaddress, gmailpassword)
        mailServer.sendmail(gmailaddress, mailto, str(msg))
        print msg
        time.sleep(1000)
    else:
        print msg
        time.sleep(400)
