mob=input(input("Enter mobile number"))
mobile=lambda mob: "Mobile" if (len(mob)==10) and mob.startswith('9'or'7'or'8'or'6') else "No a mobile"
print(mobile(mob))