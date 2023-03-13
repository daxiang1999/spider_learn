import requests
import pandas

reg = requests.get("http://xtuxiang.info/index.php/2022/12/01/pandas%e7%ac%94%e8%ae%b0/")

with open(".\sogouwangye.html","w",encoding="utf-8") as fp:
    fp.write(reg.text)
print(reg.text)

'''
dfs = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh_TW")
print(dfs[0])
'''



