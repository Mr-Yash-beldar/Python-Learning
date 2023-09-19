#opening closing and mode of files
f=open("yash.txt",'w')
print("File name: ",f.name)
print("File Mode: ",f.mode)
print("is Writeable: ",f.writable())
print("is readable: ",f.readable())
print("is closed: ",f.closed)
f.close()
print("is closed: ",f.closed)

