#Create a class employee having data member emp id ,emp salary, emp name and accept and display data file object in python
# write a program to create class student having data member roll no ,age ,name,clgname,display data of 10 objects in python
# crete class area in which find out area of circle area of rectangle area of tragnle using functions
# write aprogram to crate class city in which display info about city (doc fun) and also display rank and name of city us init fucn and string function
class Employee:
    def __init__(self, emp_id, emp_salary, emp_name):
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_name = emp_name

    def accept_data(self):
        try:
            with open("employee_data.txt", "a") as file:
                file.write(f"Employee ID: {self.emp_id}\n")
                file.write(f"Employee Salary: {self.emp_salary}\n")
                file.write(f"Employee Name: {self.emp_name}\n")
                file.write("\n")
            print("Data saved successfully to employee_data.txt")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def display_data():
        try:
            with open("employee_data.txt", "r") as file:
                data = file.read()
                if data:
                    print(data)
                else:
                    print("No data found in employee_data.txt")
        except FileNotFoundError:
            print("Employee data file not found.")

# Usage example
emp1 = Employee("E001", 50000, "John Doe")
emp1.accept_data()

emp2 = Employee("E002", 60000, "Jane Smith")
emp2.accept_data()

Employee.display_data()
