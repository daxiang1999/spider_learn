import requests


url = "https://www.sogou.com/web"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}
wd = input("enter a world!")
param = {
    "query": wd
}
reg = requests.get(url,params=param,headers=headers)

print(reg.text)
