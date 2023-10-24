# 전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        # 멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        # self 누락
        print(str)
        # self 반영
        # print(self.str)

g = GString()
g.set("First Message")
g.print()
