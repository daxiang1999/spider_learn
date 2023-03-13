# 实例化一个BeautifulSoup对象，平且将页面源码数据加载到该对象
# 通过BeautifulSoup对象中相关的属性或者是方法进行标签定位和数据提取
'''
加载本地的html对象
fp = open("./test.html",'r',encoding='utf-8')
soup = BeautifulSoup(fp,'lxml')
加载从服务器上获取的html对象
response = requests.get(url).text
soup = BeautifulSoup(response,'lxml')
-- soup.tagName  返回在文档中第一次出现的tagName对应的标签
    -- soup.div   soup.a    soup.head
-- soup.find('tagName')  与 soup.tagName 类型，也是返回文档中第一次出现tagName
    -- soup.find('div')   -- soup.find('a')
    soup.find() 还可以通过属性进行定位
    soup.find('div',class_='song')

-- soup.find_all('tagName') :返回符合要求的所有标签，返回一个列表
    soup.find_all('a')  : 返回所有的 a 标签
    soup.find_all() 还可以通过属性进行定位
    soup.find_all('div',class_='song')

-- select:
    -- select("某种选择器(id,class,标签...选择器)") 返回的是一个列表
    -- 层级选择器：
        -- soup.select(".tang > ul > li > a")  : >表示一个层级
        -- soup.select(".tang > ul a") : 空格表示多个层级

-- 获得标签中间的文本数据
    -- soup.a.text/string/get_text()
    -- soup.a.text/get_text()  可以获取该标签下所有的文本内容，即使文本内容不是该标签下直系的文本
    -- soup.a.string    只可以获取该标签下直系的文本内容
-- 获取标签中的属性值
    -- soup.a['href']  直接使用中括号，里面添加'属性名称'






'''

from bs4 import BeautifulSoup
