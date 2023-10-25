class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print(f"Info(Name:{self.name}, Phone NUmber{self.phoneNumber})")

    def working(self):
        print("현재 작업중...")

    def sleeping(self):
        print("현재 수면중..zzz")


class Student(Person):
    def __init__(self, name,phoneNumber, subject, studentID):
        Person.__init__(self, name,phoneNumber)
        self.subject = subject
        self.studentID = studentID
        
    def printInfo(self):
        print(f"Info(Name:{self.name}, Phone NUmber:{self.phoneNumber})")
        print(f"  ㄴ Info(학과:{self.subject}, 학번:{self.studentID})")

p = Person("전우치", "010-2222-1234")
s = Student("이순신", "010-111-1234", "빅데이터","20231122")

p.printInfo()
s.printInfo()
s.working()
s.sleeping()