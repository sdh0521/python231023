# DemoDict.py

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone)
print(len(phone))
print(phone["kim"])
print("park" in phone)
print("moon" not in phone)

# 항상 객체의 참조가 전달된다
p=phone
p["kang"]="1234"

print(p)
print(phone)
print(id(phone), id(p))

# 장비관리
device = {"아이폰":5, "아이패드":10}
#추가
device["맥북"]=15
print(device)
#수정
device["아이폰"]=6
#삭제
del device["아이패드"]
print(device)

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

print(bool(0))
print(bool(1))
print(bool("0"))
print(bool("1"))
print(bool([]))
print(bool([1,2]))

print(1>2)
print(5/2)
print(5//2)