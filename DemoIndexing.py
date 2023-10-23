# DemoIndexing.py

x = 100
y = 3.14

print(type(x))
print(type(y))

strA = "Python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))

lst = [1,2,3]
for item in lst:
    print(item)

print(strA[0])
print(strA[:6])
print(strA[-3:])

strC = """
다중라인
테스트
입니다
"""
print(strC)
print("다중라인\t을 출력")

colors = ["red","blue", "green"]
print(type(colors))
print(colors)
colors.append("yellow")
print(colors)