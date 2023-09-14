def sum(a,b):
    return a+b

s=lambda a,b:a+b
print(s(4,6))

def large(a,b):
    if a>b:
        return a
    else:
        return b

largest=lambda a,b:a if a>b else b
print(largest(9,6))
