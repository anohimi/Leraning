import urllib.request
from lxml import etree

# 1. 请求对象的定制
base_url = "https://sc.chinaz.com/tupian/dongman"

hd = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1689690967; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1689694615',
    'Host': 'sc.chinaz.com',
    'Referer': 'https://sc.chinaz.com/tupian/dongman.html',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def create_request(page):
    if page == 1:
        url = base_url+".html"
    else:
        url = base_url+"_"+str(page)+".html"

    req = urllib.request.Request(headers=hd,url = url)

    return req

def get_cont(req):
    response = urllib.request.urlopen(req)

    content = response.read().decode('utf-8')

    return content

def analyse_cont(content):
    tr = etree.HTML(content)



    # 涉及图片的网站一般使用懒加载技术
    picSrcList = tr.xpath('//div[@class="container"]//img/@data-original')

    picNameList = tr.xpath('/html/body/div[3]/div[2]//img/@alt')

    # print(len(picSrcList),len(picNameList))


    for i in range(0,len(picSrcList)):
         pic = urllib.request.urlretrieve('https:'+picSrcList[i],'./zzsc/'+picNameList[i]+'.jpg')


# 2. 获取网页的源码
# 3. 下载

if __name__ == '__main__':

    start_page = eval(input("请输入起始页码:"))

    end_page = eval(input("请输入结束页码:"))

    for i in range(start_page,end_page+1):
        req = create_request(i)
        con = get_cont(req)
        analyse_cont(con)