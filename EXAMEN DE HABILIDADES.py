import json
import requests
requests.packages.urllib3.disable_warnings()
import urllib.parse

api_url="http://api.meraki.com/api/v1/organizations"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

resp = requests.get(api_url,headers=headers,verify=False)
print("Request status:",resp.status_code)

response_json = resp.json()
print(json.dumps(response_json, indent=4))

main_api="https://api.meraki.com/api/v1/organizations"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

Organizacion=463308
Redes="/networks"

api_url2=main_api + urllib.parse.urlencode({"/":Organizacion})+Redes

resp2 = requests.get(api_url2,headers=headers,verify=False)
print("Request status:",resp2.status_code)

response_json2 = resp2.json()
print(json.dumps(response_json2, indent=4))
