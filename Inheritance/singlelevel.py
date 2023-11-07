class Parent:
    def showParent(self):
        print("It's Parent Class")

class Child(Parent):
    def showChild(self):
        print("It's Child of Parent Class")

parent=Parent()
parent.showParent()
child=Child()
print('-'*30)
child.showParent()
child.showChild()