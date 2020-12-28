
import requests
import json

class Nse:
    def __init__(self):
        print("NSE is initialising ....")
        self.session = self.get_session()

    def session_call(self, url):
        return self.session.get(url, headers=self.headers(), data= {})

    def get_session(self):
        session = requests.Session()
        url = "https://www.nseindia.com/"
        payload = {}
        session.get(url, headers=self.headers(), data = payload)
        return session

    def pp(self, response):
        print(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
    def get_corporate_info(self):
        url = 'https://www.nseindia.com/api/quote-equity?symbol=YESBANK&section=corp_info'
        response = self.session_call(url)
        self.pp(response)

    def get_block_deals(self):
        url = 'https://www.nseindia.com/api/quote-equity?symbol=YESBANK&section=trade_info'
        response = self.session_call( url )
        self.pp(response)

    def headers(self):
        """
        Builds right set of headers for requesting http://nseindia.com
        :return: a dict with http headers
        """
        return {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
nse_object = Nse()
nse_object.get_corporate_info()
nse_object.get_block_deals()