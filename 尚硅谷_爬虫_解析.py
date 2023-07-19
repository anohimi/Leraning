import urllib.request

import lxml.etree
from lxml import etree

# xpath解析   ---   xpath返回的对象是一个列表类型的数据
# 1. 本地文件   etree.parse()
# 2. 服务器响应的数据   --->   response.read().decode('utf-8')   etree.HTML()

# 解析本地文件
tr = etree.parse('xpath解析本地文件.html')

# tr.xpath('xpath路径')

# 查找所有ul下面的li   ---   路径查询
# //:查找所有子孙节点   一路找到底
# /:查找直接子节点   只找下一级
# list = tr.xpath("//ul/li/text()")
# print(list)

# 查找所有有id的li属性   ---
#       谓词模糊查询   只要有指定的谓词就可以
# list_id = tr.xpath("//ul/li[@id]/text()")
# print(list_id)
#
# # 查找所以id为l1的li标签   ---
# #        谓词精准     查询注意引号问题
# list_id1 = tr.xpath("//ul//li[@id='l1']/text()")
# print(list_id1)
#
# # 查询class为c1的标签
# list_c1 = tr.xpath("//ul/li[@class='c1']/text()")
# print(list_c1)
#
# # 查找到id为l2的标签的class的属性值
# obj = tr.xpath("//ul/li[@id='l2']/@class")
# print(obj)
#
# # 查找id包含l的标签
# list_cl = tr.xpath("//ul//li[contains(@id,'l')]/text()")
# print(list_cl)
#
# list_sg = tr.xpath("//ul/li[starts-with(@id,'g')]/text()")
# print(list_sg)
#
# # 查询id为l1,class为c1的标签
# list_candl = tr.xpath("//ul/li[@id='l1' and @class='c1']/text()")
# print(list_candl)
#
# # 查询id包含l或class为shanghai的标签   模糊查询  or要分为两个查找来写
# list_lorsh = tr.xpath("//ul/li[contains(@id,'l')]/text() | //ul/li[@class='shanghai']/text()")
# print(list_lorsh)

# 获取百度网页的百度一下

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url=url)

content = response.read().decode('utf-8')

# 解析网页源码
tree = etree.HTML(content)

ls = tree.xpath("//input[@id='su']/@value")

print(ls[0])

