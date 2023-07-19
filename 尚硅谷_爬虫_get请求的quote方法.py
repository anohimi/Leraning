# 需求:
# 获取
# https://www.baidu.com/s?wd=周杰伦的网页源码

import urllib.request

url = 'https://www.baidu.com/s?wd='

# 请求对象的定制   ---   为了解决反爬的第一种手段   ---   UA模拟

headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# # 请求对象的定制
# request = urllib.request.Request(url=url,headers=headers)
#
# # 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)
#
# # 显示相应的内容
# print(response.read().decode('utf-8'))


# 将ascii字符转换为unicode
# 导入必需的模块
import urllib.parse

name = urllib.parse.quote('周杰伦')
url = url + name

request = urllib.request.Request(url=url,headers=headers)

print(urllib.request.urlopen(request).read().decode('utf-8'))

print(name)
