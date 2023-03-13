import requests
import json

url = "https://movie.douban.com/j/chart/top_list"

params = {
    "type": "30",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "100"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

response = requests.get(url, params=params, headers=headers)
data_list = response.json()
fp = open(".\豆瓣评分.json","w",encoding="utf-8")
json.dump(data_list,fp,ensure_ascii=False)
print(response.json())
