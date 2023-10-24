class Person:
    #initialize Method
    def __init__(self):
        #Initialize Member Value
        self.name = "default Name"

    #Member Method
    def print(self):
        print(f"My name is {self.name}")

#Create Instance
p1 = Person()
p2 = Person()
p1.name = "전우치"
#Call Method
p1.print()
p2.print()

#런타임시에 변수 추가
Person.title = "new title"
print(p2.title)
print(Person.title)
print(p1.title)

