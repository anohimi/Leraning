import urllib.request

url = 'https://www.baidu.com'

# url的组成
# 1.协议   ---   http/https
# 2.主机   ---   域名
# 3.端口   ---   80/443...
# 4.路径
# 5.参数
# 6.锚点

response = urllib.request.urlopen(url)
print(response.read().decode('utf-8')) #UA反扒

headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# 请求对象的定制   ---   因为urlopen方法中不能存储字段
request = urllib.request.Request(url=url,headers=headers)
res1 = urllib.request.urlopen(request)
print(res1.read().decode('utf-8'))
