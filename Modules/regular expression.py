import re

txt=input("Enter text")
pattern =input("Enter text")

val=re.match(pattern,txt)
print(val)

# pattern =r'\d'
# text="Yash 123 beldar"

# match=re.search(pattern,text)
# print(match)

# pattern =r'[A-Za-z]+ions'
# text="Lions are live in Jions Lions are vions nions harmfull animal In India Lions are rare animal"

# match=re.findall(pattern,text)
# print(match)

# pattern =r'[A-Za-z]+ions'
# text="Lions are live in Jions Lions are vions nions harmfull animal In India Lions are rare animal"

# match=re.sub(pattern,"X",text)
# print(match)

# pattern =r'\w'
# text="Lions are live in Jions Lions are vions nions harmfull animal In India Lions are rare animal"

# match=re.split(pattern,text)
# print(match)