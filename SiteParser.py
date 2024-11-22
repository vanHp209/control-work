
import urllib3
from bs4 import BeautifulSoup

class SiteParser:
    """Клас для пошуку інформації на сайтах."""

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-IN,en;q=0.9',
        'cache-control': 'no-cache',
        'dnt': '1',  # Заголовок запиту "Do Not Track"
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.114", "Google Chrome";v="126.0.6478.114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '"6.5.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    http = urllib3.PoolManager()

    def search(self, sites_list, query):
        result = {}
        for site in sites_list:
            response = self.http.request('GET', site, headers=self.headers, redirect=True )
            # print(response.data.decode('utf-8'))
            soup = BeautifulSoup(response.data, 'html.parser')
            result[site] = len(soup.body.findAll(text=query))
        return result


# sites = [ ]
#
# site_parser = SiteParser()
# res = site_parser.search(sites, 'Дедпул')
# print(res)
