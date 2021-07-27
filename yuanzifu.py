import re
#
# r = re.findall("\w+@\w+\.\w+", "hello, this is a test, wangxiaomi888@126.com, 359550330@qq.org")
# print(r)
#
# r = re.findall(r"\b[A-Z]\w*", "Hello I A BCD iPython")
# print(r)
#
# r = re.findall("\d+\.?\d+", "123.23 34 12.56")
# print(r)
#
# r = re.findall(r"\b9", r"\d 98")
# print(r)
#
# r = re.findall(r"\(.+?.\)", "(#06#)是一个(特殊代码)")
# print(r)
#
# r = re.search(r"(ab)*", r"abababababa").group()
# print(r)
#
# r = re.search(r"(王|李)\w+", "王刚,李娜，").group(1)
# print(r)

# r=re.search(r"(?P<dog>ab)cdefg","abcdefghtyu").group("dog")
# print(r)

r=re.findall(r"-?\d+\.?/?\d+%?","12 1.6 11.5 -5 46.8% 1/3")
print(r)

r=re.findall(r"\d{17}\d|\d{17}x|\d{17}X","32108119890630781x")
print(r)


print("工作区发生了变动")

print("master分支修改了此文件")


