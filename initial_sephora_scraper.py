import requests
import time

url = 'https://api.bazaarvoice.com/data/reviews.json'

params = {
  'Filter': 'ProductId:P39787544',
  'Sort': 'Helpfulness:desc',
  'Limit': 30,
  'Offset': 0,
  'Include': 'Products,Comments',
  'Stats': 'Reviews',
  'passkey': 'rwbw526r2e7spptqd2qzbkp7',
  'apiversion': 5.4
}

reviews = []
loop = 0

while True:
    params['Offset'] = len(reviews)
    
    r = requests.get(url, params=params)

    if (r.status_code != 200) or (len(reviews) >= r.json()['TotalResults']):
        break

    reviews.extend(r.json()['Results'])

    time.sleep(0.5)

    print(len(reviews))
