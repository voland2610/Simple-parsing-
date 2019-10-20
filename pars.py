import requests
from bs4 import BeautifulSoup as bs

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36',
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"}

b_url = "https://malvina-club.ru/hours/"


def pars_info():
    session = requests.Session()
    request = session.get(b_url, headers=headers)

    if request.status_code == 200:

        soup = bs(request.content, "lxml")
        hours_table = soup.find('table', attrs={"id": "hours_table"})

        girl_info = hours_table.find_all('tr', attrs={"class": "hours"})

        for girl in girl_info:
            hours = [x["data-hours"] for x in girl.find_all("td", {"data-rest": "false"})]
            date = [x["data-date"] for x in girl.find_all("td", {"data-rest": "false"})]
            work_time = dict(zip(date, hours))

            data = {
                "name": girl.span.text,
                "work_time": work_time,

            }

            print(data)


pars_info()
