import requests
import json

url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

data = {
    "kw": "dog"
}
response = requests.post(url, data=data, headers=headers)
dic_obj = response.json()
fp = open(".\百度翻译.txt", "w", encoding="utf-8")
json.dump(dic_obj, fp, ensure_ascii=False)