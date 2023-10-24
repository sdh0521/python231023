# ChatGPT 로 생성한 코드
# 파이썬으로 클래스를 코딩하는데 Person 클래스는 id, phoneNumber 변수가 있고, printInfo() 메서드가 해당 변수를 출력하는 메서드이다. Person 클래스의 파생클래스인 Manager에는 skill ㅕㅂ누사 추가되고, Employee 클래스는 파생클래스인데 title 변수가 추가되는 형태로 클래스 코드를 작성해서 샘플 코드까지 생성해줘

class Person:
    def __init__(self, id, phoneNumber):
        self.id = id
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print(f"ID: {self.id}")
        print(f"Phone Number: {self.phoneNumber}")

class Manager(Person):
    def __init__(self, id, phoneNumber, skill, title):
        super().__init__(id, phoneNumber)
        self.skill = skill
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")
        print(f"Title: {self.title}")

class Employee(Manager):
    def __init__(self, id, phoneNumber, skill, title, department):
        super().__init__(id, phoneNumber, skill, title)
        self.department = department

    def printInfo(self):
        super().printInfo()
        print(f"Department: {self.department}")

# Sample code to create instances of the classes and print their information
person = Person("12345", "555-555-5555")
person.printInfo()

print("\n")

manager = Manager("54321", "444-444-4444", "NUSA", "Senior Manager")
manager.printInfo()

print("\n")

employee = Employee("98765", "777-777-7777", "NUSA", "Junior Manager", "HR")
employee.printInfo()
