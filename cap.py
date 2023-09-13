sem = int(input("Enter no of semester = "))
temp = []
marks = []
maxmarks = []
for i in range(1, sem+1):
    semno = int(input("Enter no of subjects in {} semester = ".format(i)))
    temp.append(semno)


for i in range(1, sem+1):
    print("\nMarks obtain in semester {}".format(i))
    for j in range(1, temp[i-1]+1):
        mark = int(input("enter a subject {} marks = ".format(j)))
        if (mark > 100):
            print("enter marks under 100 ")
            mark = int(input("enter a subject {} marks = ".format(j)))
        marks.append(mark)

    maxmarks.append(max(marks))
    marks.clear()

for i in range(1, sem+1):
    print("\nMaximum marks in semester {} ".format(i))
    print(maxmarks[i-1])
