class Employee:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.salary = 0.0

    def work():
        print("Complete UMatters Work")

    def setDetails(self, name, id):
        self.name = name
        self.id = id 
    
    def getSalary(self)->float:
        return self.salary


class HRManager(Employee):
    def giveSalary(self, amount):
        self.salary = amount

    def work():
        # super().work()
        print("Working Fast and Efficiently")

    def addEmployee(Employee):
        Employee.name=input("Enter name of the Employee: ")
        Employee.id=int(input("Enter ID of the Employee: "))

        
        

test=HRManager()
test.addEmployee()
test.giveSalary(10000.00)
# test.work()
print(test.getSalary())






