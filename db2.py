# db1.py

import sqlite3

# 파일에 저장
con=sqlite3.connect("c:\\work\\sample.db")
cur=con.cursor()
cur.execute("""create table if not exists PhoneBook
            (id integer primary key autoincrement, name text, phoneNum text);
            """)

cur.execute("insert into PhoneBook (name, phoneNum) values ('전우치', '010-123');")

# 입력 파라메타 처리
name="홍길동"
phoneNum="010-333"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);", (name, phoneNum))

# 다중으로 행을 입력
datalist=(("박문수", "010-456"), ("김철수", "010-555"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", datalist)

cur.execute("select * from PhoneBook;")
# for row in cur:
    # print(row)
    
# for row in list(cur):
#     print(row)

# print("fetchone: ", cur.fetchone())
# print("fetchmany: ", cur.fetchmany(2))
print("fetchall: ", cur.fetchall())

con.commit()