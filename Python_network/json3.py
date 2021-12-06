import urllib.request as rq
import json
import datetime, pprint

url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1"

# http통신 클라이언트에서 request를 보내면 서버에서 response가 이뤄짐
with rq.urlopen(url) as ur:
    data = json.loads(ur.read().decode())
    print(data)

print("\n=============== json pharsing ==============\n")
name = data["name"]
print("도시명 : ", name)

dt = data["dt"]
print("데이터 저장 시간 : ", datetime.datetime.fromtimestamp(int(dt)).strftime("%Y-%m=%d %H:%M:%S"))
print("\n")

main = data["main"]
temp = main["temp"]
print("온도 : ", int(temp) - 273.15)
print("\n")

weather = data["weather"]
main = weather[0]
print(main["main"])
print(main["description"])
