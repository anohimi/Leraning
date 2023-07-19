import urllib.parse
import urllib.request

base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

ua_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def create_request(page,city):
    base_data1 = {
        'cname': city,
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }

    data = urllib.parse.urlencode(base_data1).encode('utf-8')

    request = urllib.request.Request(data=data,headers=ua_header,url=base_url)

    return request

def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content

def down_load(content,page):
    with open('KFC'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)
    fp.close()

if __name__ == '__main__':
    start_page = eval(input("请输入起始页码:"))
    end_page = eval(input("请输入结束页码:"))
    city = input("请输入想要查询的城市:")

    for page in range(start_page,end_page+1):
        req = create_request(page,city)
        con = get_content(req)
        down_load(content=con,page=page)