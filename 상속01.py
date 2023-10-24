# 부모 클래스

# class Person(object):
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

    def working(self):
        print("작업중")

    def sleeping(self):
        print("수면중")

# 자식 클래스
class Student(Person):
    # 초기화 메서드 재정의
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    def printInfo(self):
        Person.printInfo(self)
        print("info(학과:{0}, 학번: {1})".format(self.subject, self.studentID))

    def working(self):
        Person.working(self)
        print("w")
        

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")

# print(p.__dict__)
# print(s.__dict__)

p.printInfo()
s.printInfo()
# p.working()
s.working()