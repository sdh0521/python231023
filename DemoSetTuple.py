# DemoSetTuple.py

a={1,2,3,3}
b={3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
#print(a[0])

# Tuple
tp=(1,2,3)
print(tp)
print(len(tp))
print(tp[0])
print("id: %s, name: %s, other: %s" % ("kim", "김ㅇ신","aaa"))
print(type(tp))

#함수정의
def calc(a,b):
    return a+b, a*b

#함수호출
print(calc(3,4))
args=(4,5)
calc(*args)