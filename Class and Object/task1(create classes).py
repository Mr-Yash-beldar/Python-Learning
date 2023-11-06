class Time:
    def __init__(self):
        self.time = "Morning"

    def showtime(self):
        print(f"It's {self.time} time now")

class Date:
    def __init__(self):
        self.date = "6 Oct 2023"

    def showdate(self):
        print(f"Date is {self.date}")


class Person:
    def __init__(self):
        self.person_name = "Yashodip Beldar"

    def introduce(self):
        print(f"Hi... This is {self.person_name} ")

class Student:
    def __init__(self):
        self.student_branch = "Computer"

    def branch(self):
        print(f"I am from {self.student_branch} branch")

class Fan:
    def __init__(self):
        self.fan = "Shree Krishna"

    def krishna(self):
        print(f"I am a fan of {self.fan} ")

class Point:
    def __init__(self):
        self.pointer = "7.3 CGPA"

    def CGPA(self):
        print(f"I have  {self.pointer} now ")

class Box:
    def __init__(self):
        self.box_thinking = '''Out of the "Box" '''

    def more(self):
        print(f"I always think  {self.box_thinking}  ")

time=Time()
time.showtime()

date=Date()
date.showdate()

person=Person()
person.introduce()

student=Student()
student.branch()

fan=Fan()
fan.krishna()

pointer=Point()
pointer.CGPA()

thinking=Box()
thinking.more();



