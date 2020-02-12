import requests

serviceKey = 't6nsPErSmxNTxAxnAxyX28EglD3h0muCKGhCpz7SpVKyaGlikyXgWo7t8P49TWixaumnRKIicnR%2F4h9okhEfMw%3D%3D'

endpoint = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/areaCode?serviceKey={}&numOfRows=10&pageSize=10&pageNo={}&MobileOS=ETC&MobileApp=AppTest&_type=json'.format(serviceKey,1)


resp = requests.get(endpoint)
print(resp.status_code)
print(resp.text)

data = resp.json()
print(data['response']['body']['items']['item'][0])




