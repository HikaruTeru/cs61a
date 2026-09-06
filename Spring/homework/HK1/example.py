
from urllib.request import urlopen
# import 语句：从标准库加载模块，使 urlopen 函数在当前命名空间中可用

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
# 赋值语句：调用 urlopen 函数，将返回的响应对象绑定到名称 shakespeare
# urlopen 将 URL 背后的 HTTP 请求、连接管理等复杂性封装在函数内部

words = set(shakespeare.read().decode().split())
# 方法链（method chaining）调用：
#   .read()   — 读取字节流（bytes）
#   .decode() — 将字节流解码为字符串（str），默认 UTF-8
#   .split()  — 按空白字符切分为单词列表（list）
#   set()     — 去重，构造集合（set）对象，共 33,721 个唯一词

result = {w for w in words if len(w) == 6 and w[::-1] in words}
# 集合推导式（set comprehension）：
#   w[::-1] 使用切片（slice）步长为 -1，将字符串反转
#   筛选出长度为 6 且其逆序也存在于集合中的单词
print(result)
# {'redder', 'drawer', 'reward', 'diaper', 'repaid'}




from urllib.request import urlopen

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
words = set(shakespeare.read().decode().split())
result = {w for w in words if len(w) == 6 and w[::-1] in words}

print(result)


