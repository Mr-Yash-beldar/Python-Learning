# Task 3 With BPL

class ElectricityBill:
    def __init__(self,name,units,isunderBPL): 
        self.name=name
        self.units=units
        self.isunderBPL=isunderBPL

    
    def needToPay(self)->float:
        bill=0.0

        if(self.isunderBPL and self.units<=200):
            return bill
        
        else:
            units=self.units
            for unit in range (units+1):
                if(unit <=30):
                    bill=bill+1.50
                elif(unit >30 and bill<=300):
                    bill=bill+3.00
                else:
                    bill=bill+4.25
                    
            if(bill>500):
                bill=bill+((bill*15)/100)

            return bill

    
    def display(self):
        print(f"{self.name:<15} {self.units:<10} {self.needToPay():<10} ")


Users=[
    ElectricityBill("Rushi",330,False),
    ElectricityBill("Yashodip",450,True),
    ElectricityBill("Harsh",500,True),
    ElectricityBill("Paresh",200,True),
    ElectricityBill("Gopal",30,False)

]

print("\n")
print(f"{'Name of User':<15} {'units':<10} {'bill':<10} ")
print("-" * 35)
for user in Users:
    user.display()




        