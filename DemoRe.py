# DemoRe.py

import re

result=re.search("[0-9]*th", " 35th")
print(result)
print(result.group())

# result=re.match("[0-9]*th", " 35th")
# print(result)
# print(result.group())

result=re.search("apple", "this is Apple".lower())
print(result.group())

result=re.search("\d{4}", "올해는 2023년입니다")
print(result.group())

result=re.search("\d{5}", "우리 동네 주소는 52300")
print(result.group())
print(result.span())

data="Apple is big company and apple is delicious"
c=re.compile("apple", re.IGNORECASE)
print(c.findall(data))

data="""다중 라인으로
만든 문자열

데이터"""
c=re.compile("^.+", re.MULTILINE)
print(c.findall(data))

