# urlencode方法应用场景 : 请求时需要多个参数

# https://www.baidu.com/s?wd=周杰伦&sex=男

import urllib.parse

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

a = urllib.parse.urlencode(data)
print(a)