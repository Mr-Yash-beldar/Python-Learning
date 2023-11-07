class GrandFather:
    def showGrandFather(self):
        print("GrandFather Class")

class Father(GrandFather):
    def showFather(self):
        print("Father Class")

class Child(Father):
    def showChild(self):
        print("Child Class")

child=Child()
child.showGrandFather()
print('-'*30)
child.showFather()
print('-'*30)
child.showChild()

