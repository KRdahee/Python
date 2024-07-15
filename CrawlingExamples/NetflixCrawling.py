import requests
from bs4 import BeautifulSoup as bs

req = requests.get("https://flixpatrol.com/top10/netflix/world/today/full/#netflix-2")
html = req.text
soup = bs(html, "lxml")

mediaContents = soup.select("#netflix-2 > div.-mx-content > div > div > table > tbody > tr")
rownum=1

for content in mediaContents:
    try:
        contentTitle = content.select_one("td:nth-child(3)").text
        contentPoint = content.select_one("td:nth-child(4)").text
        contentChange = content.select_one("td:nth-child(5)").text
        contentCountries = content.select_one("td:nth-child(6)").text
        contentXcountry = content.select_one("td:nth-child(7)").text
        contentDays = content.select_one("td:nth-child(8)").text
        contentXday = content.select_one("td:nth-child(9)").text
        contentTotal = content.select_one("td:nth-child(10)").text
        print(str(rownum) +' : '+ contentTitle.strip() +' | '+ contentPoint +' | '
            + contentChange +' | '+ contentCountries +' | '+ contentXcountry +' | '
            + contentDays +' | '+ contentXday +' | '+ contentTotal)
        rownum += 1
    except AttributeError:
        continue