import requests
from bs4 import BeautifulSoup as bs
from twilio.rest import Client
import threading

def currency():
    threading.Timer(300.0, currency).start()
    account_sid = "ACdc897247e82666fee0953f763b5a7060"
    auth_token  = "d6e4fd8848fe45f3784b4ba35a11c5f6"

    ethurl = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
    urlget = requests.get(ethurl)
    urltext = urlget.text
    ethexbs = bs(urltext,"html.parser")

    sendstr=ethexbs.text
    redtext = "{,},\",:"
    for char in redtext:
        sendstr=sendstr.replace(char," ").strip()
    sendstrspl=sendstr.split("  ")
    sendstr=' '.join(sendstrspl)
    print(sendstr)
    usdprice=float(sendstrspl[3])
    print(usdprice)
    if usdprice > 300:
        print("Alert -- Price above required index - SELL!!!! -- (SMS being sent to User) ")
        client = Client(account_sid, auth_token)
        message = client.messages.create(to="+918347824246",from_="+12244791958",body=sendstr)
        print(message.sid)
    elif usdprice < 250:
        print("Alert -- Price below required index - BUY!!!! -- (SMS being sent to User) ")
        client = Client(account_sid, auth_token)
        message = client.messages.create(to="+918347824246", from_="+12244791958", body=sendstr)
        print(message.sid)

currency()