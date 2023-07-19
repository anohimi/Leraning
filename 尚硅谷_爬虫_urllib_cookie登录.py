# QQ空间为例

# 使用场景:数据采集需要绕过登录

import urllib.request

url = 'https://user.qzone.qq.com/1405774857'

headers = {
    # ':Authority': 'user.qzone.qq.com',
    # ':Method': 'GET',
    # ':Path': '/1405774857',
    # ':Scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Cache-Control': 'max-age=0',
    # cookie中包含着登录信息
    'Cookie': 'LW_uid=a186t7e9v9G2z5d9k1S4D0n9K0; eas_sid=f1I6O7L959R205c9I114K0P9h7; pgv_pvid=9273245843; LW_sid=c136f7i9A9w3b1k3N0m9x7l9B3; RK=6heUUbP9Xm; ptcz=916bb1f2a74b37a07ade0ac3dff4e87c48f41117c8a7abe25e9e63b06fafcd22; _qpsvr_localtk=0.041974525204609536; pgv_info=ssid=s9056294688; ptui_loginuin=1405774857; uin=o1405774857; skey=@qqMGniZbj; p_uin=o1405774857; pt4_token=dFrHNmwGdR63rGj68P5MdOubIEflx3Pl9Cb7ievmyuk_; p_skey=kqrJnTEUirMpzVC8CKlFOpxuNR0vuI4jjRaGCzr1HVE_; Loading=Yes; qz_screen=1280x720; QZ_FE_WEBP_SUPPORT=1',
    # 'If-Modified-Since:Wed, 12 Jul 2023 14:20': '02 GMT',

    # refer用于判断是否从上一路径中进入
    'Referer': 'https//qzs.qq.com/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

req = urllib.request.Request(url=url,headers=headers)

res = urllib.request.urlopen(req)

content = res.read().decode('utf-8')

with open('qq zone.html','w',encoding='utf-8') as fp:
    fp.write(content)