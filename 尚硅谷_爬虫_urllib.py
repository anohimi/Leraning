# 使用urllib来获取百度首页的源码

import urllib.request

# 定义一个url --- 想要访问的地址
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(url)

# 获取响应中的页面的源码
# read方法  返回的是字节形式的二进制数据
# 需要将二进制的数据转换为字符转
# 二进制   -->   字符串   解码  decode('编码的格式')
# content = response.read().decode('utf-8')

# 打印数据
# print(content)

# 1个类型和6个方法

# 模拟浏览器想服务器发送请求
response = urllib.request.urlopen(url)

# 1个类型
# response是HTTPResponse类型
print(type(response))

#read方法  ---   无传参时一个一个字节进行读取,有传参时读取参数指定的字节数  read()和read(num)

# readline方法  ---  读取一行

# readlines方法  ---  读取多行,直至读完

# getcode  ---  返回状态码

# geturl  ---   返回url地址
print(response.geturl())

# getheaders  ---  返回一个状态信息

# 1个类型   ---   response的类型是HTTPResponse
# 6个方法   ---   read()  readline()  readlines()  getcode()  geturl()  getheaders()

# 下载   ---   urllib.request().urlretrive(url,filename)

# 下载网页
# url_page = 'http://www.baidu.com'
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
url_img = 'https://img0.baidu.com/it/u=1127711128,1465358813&fm=253&fmt=auto&app=138&f=JPEG?w=600&h=338'

urllib.request.urlretrieve(url_img,'lol.jpg')

# 下载视频