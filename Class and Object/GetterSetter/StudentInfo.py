class Student:
    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    
    def setPercentage(self,per):
        self.per=per
    
    def getPercentage(self):
        return self.per
    
student=Student()
n=int(input("Enter number of Student: "))
for i in range (n+1):
    name=input("Enter Student Name: ")
    student.setName(name)
    per=float(input("Enter Student Percentage: "))
    student.setPercentage(per)
    print(f"Hi {student.getName()} Your percentage are is {student.getPercentage()}")
    print("\n")
    