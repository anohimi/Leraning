import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Acs-Token': '1688995270926_1688995271398_KToFInwnawgERvzpBWol+7Zjqm0cQOYLsgHrU1G0mm9UYXRJWYIMz/CxJJadfSTX9wUUrMeUY7NeOZiYWXwR0FuDDffmLMZ8UpYluMAbkIshbRdj7xVweNOjs62wOdd83VU2jih0XlE7MtGEUjisWahEnoHmlF2bgbiLVOwSia4CnjJ4DvaGh5iA3p7JELZMmQT2PbLIdsi7HT3mY1AindbhDV8rPBRoeAc2YThtYpD8sU+fWZrBbiugF7ft8GvVbtxLnsNznHzQ0HME6eqYpi2onFLMTvGDyz1E0TlOx4H5vuTbR/0kV3kMNS4o0dBYyOs5Jp7J1V9X3/hUKNX7RMNPSR5tXYgj1+0fGfBlxcrnG1OKHR7RrDg/d/E9lbZSmIPvAaf/cOjMMRoBu2b1LSq6E7NPc6b6fUCRvfpdHweqdj2yt9DbTwE3fIZPnJc98odzEx/YBq7QD6fk+rLIbn9/AO/CSuah6QUiLsF1ZZU6xcgHTyQ0/Fy/gmoedTbS',
    'Connection': 'keep-alive',
    'Content-Length': '133',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=9C0BBA93CC10E3A9ADB1757B7FCD8620; PSTM=1679503265; BAIDUID=9C0BBA93CC10E3A988FDEBD84B8909A9:FG=1; BDUSS_BFESS=lZXVXdWVEI5OWhlZlVsME02ZW5qcmM3R0VJZG5HWEVXMFJza0tabmF4UXV1a3RrSUFBQUFBJCQAAAAAAAAAAAEAAADM5wg519TQwsrAvee1xMmtwdYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4tJGQuLSRkY; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=9C0BBA93CC10E3A988FDEBD84B8909A9:FG=1; ZFY=yghdoKdOshQ:A0XRPkEXYOX2ioMNUQNy6SbpWuc7OC4M:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; delPer=0; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1688908686; BA_HECTOR=0ga480848l050h848l0k8kas1iao0so1o; H_PS_PSSID=36549_38643_38831_39026_39023_38943_38858_38908_38954_39009_39013_39040_38920_38804_38639_26350_39041_38948_39045; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1688996425; ab_sr=1.0.1_MzY0YzVkYmYyZTFlYWUxNTQ4ZTg4ZTNkMGE0ZjRmOWIyYmFhOGUzZjczZWYxNTAyNDE5NjEyN2Y1MmUxMjM1ZTk1NDliMTA2OWJlYWFjYmNhYjA2ZDgwY2Q3ZWU2YzliZTNmM2JmNWMxNTljMDk0MWY4ODQ0MDE1YjBjOTkxYjgwNmNkODNlY2NlNmY2M2QzNzQxYTk4OTk1YjMzOTg0ODM1ZTE0YjcwMDJlNzliNTZhNDFkYmI4MWI1ZjgzMmM2',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

h2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

data = {
    'kw':'spider'
}

# post请求的参数必须进行编码
d1 = urllib.parse.urlencode(data)
# 编码  调用encode()方法
d1 = d1.encode('utf-8')


# post请求的参数不会拼接在url的后面,而是需要放在请求对象定制的参数中
request = urllib.request.Request(url = url,headers = h2,data = d1)

response = urllib.request.urlopen(request)

# 这是一个字符串
content = response.read().decode('utf-8')

# print(type(content))

#字符串   --->   json对象:       调用json类的loads方法
import json

obj = json.loads(content)
# print(type(obj))
# print(obj)

# post请求百度详细翻译
url_xxfy = 'http://fanyi.baidu.com/v2transapi?from=en&to=zh'

# 参数
data1 = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '169e9eba0d97c65a7e6c3cc4ec6c0692',
    'domain': 'common',
    'ts': '1688995271344',
}

# post请求的参数必须编码
data_xxfy = urllib.parse.urlencode(data1).encode('utf-8')

# q请求对象的定制
request_xxfy = urllib.request.Request(url = url_xxfy, data = data_xxfy, headers=headers)

# 模拟浏览器行为
response_xxfy = urllib.request.urlopen(request_xxfy)

content_xxfy = response_xxfy.read().decode('utf-8')

obj_xxfy = json.loads(content_xxfy)

print(obj_xxfy)
