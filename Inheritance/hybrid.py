class First:
    def showFirst(self):
        print("I am in First Class")

class Second(First):
    def showSecond(self):
        print("I am in Second Class")

class Third(First):
    def showThird(self):
        print("I am in Third Class")

class Fourth(Second,Third):
    def showFourth(self):
        print("I am in Fourth Class")



tester=Fourth()
tester.showFourth()
print('-'*30)
tester.showFirst()
print('-'*30)
tester.showSecond()
print('-'*30)
tester.showThird()


