import requests

url = "http://apiv2.jne.co.id:10102/tracing/api/list/v1/cnote/0114541900204500"

# payload = 'username=TESTAPI&api_key=25c898a9faea1a100859ecd9ef674548'
payload = {
    'username': 'TESTAPI',
    'api_key': '25c898a9faea1a100859ecd9ef674548'
}
headers = {

    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, headers=headers, data=payload)

print(response.json())
