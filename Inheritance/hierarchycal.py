class First:
    def showFirst(self):
        print("I am in First Class")

class Second(First):
    def showSecond(self):
        print("I am in Second Class")

class Third(First):
    def showThird(self):
        print("I am in Third Class")

test=Third()
test1=Second()
test.showFirst()
test.showThird()
test1.showFirst()
test1.showSecond()