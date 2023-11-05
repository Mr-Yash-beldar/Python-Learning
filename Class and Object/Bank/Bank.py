# Bank account task

class Bank:
    def __init__(self,name,acc_no,acc_type,acc_bal):
        self.name=name
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.acc_bal=acc_bal

    def deposite(self,amount):
        if(amount<=0):
            print("Invalid Amount")
        else:
            self.acc_bal=self.acc_bal+amount
            print(f"{amount} Deposited in account")
    
    def withdraw(self,amount):
        if(self.acc_bal<=0 and self.acc_bal<=amount):
            print("Insufficient Balance")
        else:
            self.acc_bal=self.acc_bal-amount
            print(f"{amount} Withdrawed for account")

    def display(self):
        print(f"User: {self.name}")
        print(f"User Account number: {self.acc_no}")
        print(f"User Account type: {self.acc_type}")
        print(f"Available Balance: {self.acc_bal}")

while(True):
    print("\nWelcome to Yes Bank")
    print("Enter 1 for Creating Acount")
    print("Enter 2 for Exit")
    choice=int(input("Enter Your choice: "))
    if(choice==1):
        name=input("Enter Users Name: ")
        acc_no=int(input("Enter Account number: "))
        acc_type=input("Enter Account Type: ")
        acc_bal=float(input("Enter Account Balance: "))
        user=Bank(name,acc_no,acc_type,acc_bal)

        while(True):
            print("\n________Menu________")
            print("Enter 1 for Display Details")
            print("Enter 2 for Deposite Amount")
            print("Enter 3 for Withdraw Amount")
            print("Enter 4 for Exit")
            menu=int(input("Enter Your choice: "))
            if(menu==1):
                user.display()
            elif(menu==2):
                amount=float(input("Enter Amount for Deposite: "))
                user.deposite(amount)
            elif(menu==3):
                amount=float(input("Enter Amount for Deposite: "))
                user.withdraw(amount)
            else:
                break

    else:
        break 

    
        
    

    
    


