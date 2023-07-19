# get请求
# 获取豆瓣电影第一页的数据并且保存

import urllib.request
import json
import urllib.parse

url_db = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

ua_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

# 1. 请求对象的定制
request_db = urllib.request.Request(headers=ua_header,url=url_db)

# 2. 获取请求响应的数据
response_db = urllib.request.urlopen(request_db)
content_db = response_db.read().decode('utf-8')

# 3. 下载数据到本地
# open方法默认使用的是gbk编码格式打开文件,写入中文数据需要显式调用encoding=utf-8
fp_db = open('douban.json','w',encoding='utf-8')
fp_db.write(content_db)
fp_db.close()

with open('douban1.json','w',encoding='utf-8') as fp:
    fp.write(content_db)

# 请求豆瓣电影的前10页

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    start = (page - 1)*20

    url = base_url+'start='+str(start)+'&limit=20'

    request_ten = urllib.request.Request(url = url,headers=ua_header)

    return request_ten

def request_page_optimized(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start':(page-1)*20,
        'limit':20
    }

    url = base_url+urllib.parse.urlencode(data)

    request_pg = urllib.request.Request(headers=ua_header,url = url)

    return request_pg

# 程序入口
if __name__ == '__main__':
    start_page = eval(input("请输入起始的页码:"))
    end_page = eval(input("请输入结束的页码:"))

    for page in range(start_page,end_page+1):
        request = create_request(page)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        fp_ten = open('douban_ten.json','a',encoding='utf-8')
        fp_ten.write(content)
        fp.close()
