# 对象 ---> 字节序列   ===   序列化
# 字节序列 ---> 对象   ===   反序列化
# 序列化:设计一套协议,将内存中的数据转化为字节序列并保存到文件中
# 反序列化:将文件中保存的数据转化为内存中的数据

import json #导入json模块

fp = open('test.txt','w')

# fp.write('hello world')

# 默认情况下,对象无法写入到文件中,如果想要写入文件中就需要序列化操作
name_list=['zs','ls','ww','zl']

# 序列化的两种方式:
# dump() --- 在将对象转化为json字符串的同时,吧转换后的字符串写入到指定的文件中:dump(object,file)
json1 = json.dump(name_list,fp)
# print("json1:%s",json1)

# dumps() --- 只具备把对象转换为json字符串的能力,不能写入到文件中,需要手动调用file.write()
# json2 = json.dumps(name_list)
# fp.write(json2)

# fp.write()

fp.close()

# 反序列化
# 将json字符串变成一个python对象
fp = open('test.txt','r')

content = fp.read()

# load --- 直接加载文件并且将其中的json字符串转换为python对象
result = json.load(fp)
print(type(result))

# loads --- 将读取出来的json字符串转换为python对象,需要先调用file.read读取文件中的内容
res = json.loads(content)
print(res)
print(type(res))