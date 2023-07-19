# 简介:urllib中的异常主要分为两类:URLError和HTTPError
# 1. HTTPError是URLError的子类
# 2. 导入的包分别是urllib.error.URLError和urllib.error.HTTPError
# 3. http错误:针对浏览器无法连接到服务器而增加出来的错误提示,引导并告诉浏览者是哪里出了问题
# 4. 通过urllib发送请求的时候,有可能会发送失败,为了代码的健壮性可以在这里加入异常的捕获和处理

import urllib.request
import urllib.error

from urllib import *

# 实例:

url = 'https://blog.csdn.net/jjjzzz2/article/details/1301308556'

ua_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

try:
    request = urllib.request.Request(url = url,headers= ua_header)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print(urllib.error.HTTPError)
except urllib.error.URLError:
    print(urllib.error.URLError)

