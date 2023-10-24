#func3.py

#Filtering Function
lst = [10, 25, 30]
interL = filter(None, lst)
for item in interL:
    print(item)

print("Case of Filtering")
def getBiggerThan20(i):
    return i > 20
interL = filter(getBiggerThan20, lst)
for item in interL:
    print(item)


#Contact Lambda
# print("----- Lambda -----")
# iterL = filter(lambda x:x>20, lst)
# for item in iterL:
#     print(item)

# score = int(input("Input Number >> "))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"
# print("Class : ", grade)

value = 5
while value > 0 : 
    print(value)
    value -= 1

lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

fruit = {"apple":100, "kiwi":200}
for item in fruit.items():
    print(item)


lst = list(range(1,11))
print(lst)
print("----- break -----")
for i in lst :
    if i > 5:
        break
    print(f"Item:{i}")

print("---- continue ----")
for i in lst:
    if i % 2 == 0:
        continue
    print(f"Item:{i}")


print("---- 수열함수 ----")
print(list(range(2000,2024)))
print(list(range(1,32)))

for i in range(10):
    print(i)

print("---- 리스트 함축 ----")
list = list(range(1,11))
print([i**3 for i in lst if i>5 if i<9])
fruit = ("apple", "orange", "kiwi")
print([len(i) for i in fruit])