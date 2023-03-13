import requests
import json


city = input("请输入需要查询的城市肯德基门店")
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

data = {
    "cname": "",
    "pid": "",
    "keyword": city,
    "pageIndex": "1",
    "pageSize": "10"
}

with open(".\肯德基门面点.json","w",encoding="utf-8") as fp:
    for i in range(26):
        j = i+1
        j = str(j)
        data = {
            "cname": "",
            "pid": "",
            "keyword": city,
            "pageIndex": j,
            "pageSize": "10"
        }
        response = requests.post(url, data=data, headers=headers)
        fp.write(response.text)



