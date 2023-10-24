# func2.py

#스코핑룰(LGB규칙)
x=1
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x=5
    return a+x

print(func2(1))

def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))
print(times(b=2))

def conURI(servr, port):
    strURL="http://" + servr + ":" + port
    return strURL

print(conURI("multi.com", "80"))
print(conURI(port="8080", servr="multi.com"))

# 가변인자: 가변적인 상황(*은 Tuple 의미)
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))

# LAMDA (함수일회성 함수, 즉흥적인 함수)
g=lambda x,y:x*y
print(g(3,4))

print((lambda x:x*x) (3))

print(globals())