# 使用handler访问百度获取网页源码

import urllib.request

url = 'http://www.baidu.com'

ua_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=url,headers=ua_header)

# handler   build_opener  open

# 1. 获取handler对象
handler = urllib.request.HTTPHandler()

# 2. 获取opener对象
opener = urllib.request.build_opener(handler)

# 3. 调用open方法
res = opener.open(request)

con = res.read().decode('utf-8')

# print(con)

# 代理服务器
url_proxy = 'http://www.ipip.net'

proxy = {
    'http':'83.229.70.166:3128'
}

# 1. 请求对象的定制
proxy_req = urllib.request.Request(url=url_proxy,headers=ua_header)

# 2. 创建ProxyHandler对象
# proxyhandler = urllib.request.ProxyHandler(proxies=proxy)
#
# proxy_opener = urllib.request.build_opener(proxyhandler)
#
# proxy_res = proxy_opener.open(proxy_req)
#
# fp = open('daili.html','w',encoding='utf-8')
#
# fp.write(proxy_res.read().decode('utf-8'))
#
# fp.close()


# 代理池
proxy_poll = [
    {'http':'125.158.26.33:545'},
    {'http':'83.229.160.79:3128'},
]

import random

pxy = random.choice(proxy_poll)

# pxy选择代理池中的一个，其余保持一致
