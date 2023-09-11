def find_triplets(x):
    for a in range(1, x+1):
        for b in range(1, x+1):
            c = x - a*b
            if c >= 1 and c <= x:
                print("{} {} {}".format(a, b, c))
                return (a, b, c)
    print(-1)
    return None

t=int(input(""))
while(t!=0):
    a =int(input())
    find_triplets(a)
    # print("\n")
    t=t-1;

