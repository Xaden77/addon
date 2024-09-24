from bs4 import BeautifulSoup
import requests

def get_rate(in_currency,out_currency):
    url=f"https://www.X-rates.com/calculator/?from={in_currency}&{out_currency}&amount=1"
    request=requests.get(url).content
    soup = BeautifulSoup(request,"html.parser").find("span",class_="ccOutputRslt").get_text()
    print(soup)
    rate=float(soup[:-4])
    return rate
get_rate("INR","USD")