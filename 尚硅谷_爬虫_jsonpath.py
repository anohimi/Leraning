# jsonpath   --->   解析json格式数据的工具

import urllib.request
import jsonpath

tpp_url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1689773094957_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

ua_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=tpp_url,headers=ua_header)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('tpp_city.json','w',encoding='utf-8') as fp:
    fp.write(content)