'''
response = requests.get()
1、response.text  返回的是字符串形式的数据
2、response.json()  返回的是json对象
3、response.content  返回的是二进制数据
'''

import requests
import re
import os

url = "http://xtuxiang.info"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

os.mkdir('./tupian')
response = requests.get(url=url, headers=headers)

print(response.text)
ex1 = 'background-image.*?"(.*?)".*?: center center;'
srcs = re.findall(ex1,response.text,re.S)
for src in srcs:
    response = requests.get(url=src,headers=headers)
    img_path = './tupian/'+"one.jpg"
    with open(img_path,'wb') as fp:
        fp.write(response.content)

print(src)
