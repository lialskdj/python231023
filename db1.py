#db1.py

import sqlite3

con = sqlite3.connect("c:\\work\\test.db")
con = sqlite3.connect(":memory:")

cur=con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook
(id integer PRIMARY KEY AUTOINCREMENT, name text, phoneNum text);""")

#1건 입력
cur.execute("""
INSERT INTO PhoneBook (name, phoneNum) 
values('전우치', '010-222');""")

#입력 파라미터 처리
name = "홍길동"
phoneNumber = "010-333"

cur.execute("""
INSERT INTO PhoneBook (name, phoneNum) 
values( ?, ?);""", (name, phoneNumber))

#다중으로 행을 입력
datalist = (("박문수", "010-333"),("김길동", "010-567"))
cur.executemany("INSERT INTO PhoneBook (name, phoneNum) values(?,?);", datalist)


#검색
cur.execute("SELECT * FROM PhoneBook")
print("---- fetchone() ----")
print(cur.fetchone())
print("---- fetchmany(2) ----")
print(cur.fetchmany(2))

cur.execute("SELECT * FROM PhoneBook")
print("---- fetchall() ----")
print(cur.fetchall())