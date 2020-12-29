
import requests
import json
import sys

class Nse:
    def __init__(self, stock_list):
        print("NSE is initialising ....")
        self.session = self.get_session()
        self.stock_list = stock_list

    def session_call(self, url):
        return self.session.get(url, headers=self.headers(), data= {})

    def get_session(self):
        session = requests.Session()
        url = "https://www.nseindia.com/"
        payload = {}
        session.get(url, headers=self.headers(), data = payload)
        return session

    def pp(self, response):
        print(json.dumps(response, indent=4, sort_keys=True))

    def get_corporate_info(self, stock_symbol):
        url = f'https://www.nseindia.com/api/quote-equity?symbol={stock_symbol}&section=corp_info'
        response = self.session_call(url)
        return response.text

    def get_block_deals(self, stock_symbol):
        url = f'https://www.nseindia.com/api/quote-equity?symbol={stock_symbol}&section=trade_info'
        response = self.session_call( url )
        return response.text

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
    
    def fetch_data_from_nse(self):
        stock_data = {}
        for stock in self.stock_list:
            stock_data['block_deals'] = json.loads( self.get_block_deals(stock) )
            stock_data['corporate_info'] = json.loads( self.get_corporate_info(stock ) )
        self.pp(stock_data)

if __name__ == '__main__':
    args = sys.argv
    print( args[1:] )
    nse_object = Nse(args[1:])
    nse_object.fetch_data_from_nse()
    # nse_object.get_corporate_info()
    # nse_object.get_block_deals()