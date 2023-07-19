# jsonpath   --->   解析json格式数据的工具
import json
import urllib.request
import jsonpath

tpp_url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1689773094957_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

cook_header = {
    'Authority': 'vip.taobao.com',
    # ':Method': 'GET',
    # ':Path': '/ajax/getGoldUser.do?_input_charset=utf-8&from=diaoding&callback=jsonp0',
    # ':Scheme': 'https',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Cookie': '_samesite_flag_=true; cookie2=11609d7eea866c08da2db08d590bcdc5; t=7ba04bc9ba90d4c89411a466fea997bb; _tb_token_=7a75efd5136be; v=0; cna=sR2iHBWUmRMCATFB+onliydz; xlly_s=1; tfstk=dwww3_67tOBZ7FPtYbM4YjtEIuHtnYQ53-gjmoqmfV0Gk5M4glaZGPZmlxz4urusiNH_3ykTd59j5NH4mzMVPa65FlEtBxb5PJICyCn1b2NpWTZTXx3zDyb5Fm8kqqjONVKP5LGcrog3Q4dmNCSj52JDU3nZsHZ6GK9XjchtrX0FQYLxxSBzH58DgfmKY4sFYSoKX_1..; l=fBIZnVynN3W8pr_MBO5Courza77TUIObzsPzaNbMiIEGa61lTF6b8NC1rSIB7dtjgTfUnetrip0J_d3JSp4p_jt_caN-1NKDCY9w-dIpQp5..; isg=BC4ucWypxq7DQzJKbGRJMhBdf4TwL_Ipei-FpFj2wDHsO8yVwLwJOe0186fX4-pB',
    'Referer': 'https://dianying.taobao.com/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

# obj = json.load(open('store.json','r',encoding='utf-8'))
#
# # 获取所有书的作者
# author_lst = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author_lst)
#
# # 获取所有的作者
# author_lst_all = jsonpath.jsonpath(obj,'$..author')
# print(author_lst_all)
#
# # 获取store的所有元素
# all_element_store = jsonpath.jsonpath(obj,'$..store.*')
# print(all_element_store)
#
# # 获取store下面所有的价格
# price_lst = jsonpath.jsonpath(obj,'$.store..price')
# print(price_lst)
#
# # 获取第三本书
# book = jsonpath.jsonpath(obj,'$.store.book[2]')
# print(book)
#
# # 获取最后一本书
# blast_lst = jsonpath.jsonpath(obj,'$.store.book[(@.length-1)]')
# print(blast_lst)
#
# # 获取前两本书
# bformertwo_lst = jsonpath.jsonpath(obj,'$..book[:2].title')
# print(bformertwo_lst)
#
# # 过滤出所有包含isbn的书
# # 条件过滤的语句在条件前面加?
# isbn_lst = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# print(isbn_lst)
#
# # 获取价格超过10元的书
# overten_blst = jsonpath.jsonpath(obj,'$..book[?(@.price > 10)].title')
# print(overten_blst)

# 解析淘票票

req = urllib.request.Request(url=tpp_url,headers=cook_header)

res = urllib.request.urlopen(req)

content = res.read().decode('utf-8')
print(type(content))

content = content.split('(')[1].split(')')

content = content[0]

with open('tpp_city.json','w',encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('tpp_city.json','r',encoding='utf-8'))
city_lst = jsonpath.jsonpath(obj,'$..regionName')
print(city_lst)