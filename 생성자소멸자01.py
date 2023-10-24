# -*- 생성자와 소멸자 -*-
class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
m=MyClass(5)
#del m
print("종료")