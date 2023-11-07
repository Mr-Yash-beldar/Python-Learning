class First:
    def showFirst(self):
        print("I am in First Class")

class Second:
    def showSecond(self):
        print("I am in Second Class")

class Third:
    def showThird(self):
        print("I am in Third Class")
class Fourth:
    def showFourth(self):
        print("I am in Fourth Class")

class Travel(First,Second,Third,Fourth):
    def travel(self):
        print("I am Traveling  Classs")


traveler=Travel()
traveler.travel()
print('-'*30)
traveler.showFirst()
print('-'*30)
traveler.showSecond()
print('-'*30)
traveler.showThird()
print('-'*30)
traveler.showFourth()

