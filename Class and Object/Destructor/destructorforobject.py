class Time:
    def __init__(self):
        print("Constructor is called")

    def __del__(self):
        print("Destructor is called")

t1=Time()
t2=Time()
del(t1)
