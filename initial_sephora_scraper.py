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

reviews = [] # each review is an element of this array (e.g. reviews[0] will display first review)
loop = 0

while True:
    params['Offset'] = len(reviews)
    
    r = requests.get(url, params=params)

    if (r.status_code != 200) or (len(reviews) >= 6):
        break

    reviews.extend(r.json()['Results'])

    time.sleep(0.5)

    print(reviews[0])
