# DemoDict.py

phone = {"Kim":"1111", "lee":"2222", "park":"3333"}

print(phone)
print(len(phone))
print(phone["Kim"])
print("park" in phone)
print("kang" not in phone)

p = phone
p["kang"] = "1234"

print(p)
print(phone)
print( id(phone), id(p) )

#장비 관리
device = {"아이폰":5, "아이패드":10}
print(device["아이폰"])
#입력
device["맥북"]=15
#수정
device["아이폰"] = 6
print(device)
#삭제
del device["아이폰"]
print(device)


print(bool(0))
print(bool(3))
print(bool(""))
print(bool('test'))
print(bool([]))
print(bool([1,2,3]))

print('----Logical Calc----')
