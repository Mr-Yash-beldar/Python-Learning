# Date:12/9/2023
#Yashodip Beldar
# Capgemini question
sems = []
marks = []
maxs = []
semister = int(input("Enter number of semister: "))
for i in range(0, semister):
    sems.append(int(input(f"Enter no of subjects in {i+1} semister: ")))

for k in range(0, semister):
    print(f"Marks obtained in semester {k+1}:")
    j=1
    while(j<sems[k]+1):
        mark = int(input())
        if (mark > 100):
            print("You have entered invalid mark")
            j=j-1
            continue
        else:
            marks.append(mark)
    maxs.append(max(marks))

for i in range(0, semister):
    print(f"Maximum mark in {i+1} semester: {maxs[i]}")
