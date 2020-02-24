import json
import requests

class SephoraData: 
    def __init__(self):
        self.productUrl = 'https://www.sephora.com/api/catalog/categories/cat60004/products?currentPage=0&pageSize=999999999&content=true&includeRegionsMap=true'
        self.reviewUrl = 'https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId%3A{product_id}&Sort=Helpfulness%3Adesc&Limit=100&Offset={offset}&Include=Products%2CComments&Stats=Reviews&passkey=rwbw526r2e7spptqd2qzbkp7&apiversion=5.4'

    def brandNames(self):
        response = requests.get(self.productUrl)

        data = json.loads(response.text)

        brand_names = [d['brandName'] for d in data['products']]

        return brand_names
    
    def productNames(self):
        response = requests.get(self.productUrl)

        data = json.loads(response.text)

        product_names = [d['displayName'] for d in data['products']]

        return product_names

if __name__ == '__main__':
    s = SephoraData()