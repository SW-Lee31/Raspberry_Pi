# json 활용
import json
from pprint import pprint

data_1 = {
    "portal_site":[
        {
            "name": "다음",
            "url": "http://www.daum.net"
        },
        {
            "name": "네이버",
            "url": "http://www.naver.com"
        }
    ],
    "mcu": {
        "core":"BCM2877"
        },
    "smartPhone":"IPhone",
    "memory":{
        "name":"Samsung-LPDDR4"
        }
    }

print("\n=================== json dump ================\n")
json_str = json.dumps(data_1)
print("json data : ", json_str)

print("\n=================== json parshing ================\n")
data_2 = json.loads(json_str)
pprint(data_2)

print(data_2["portal_site"][0]["name"])
print(data_2["portal_site"][1]["url"])
print(data_2["mcu"]["core"])
print(data_2["smartPhone"])