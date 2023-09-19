#task of copying and merging of data
f=open("file1.txt",'r')
data1=f.read()
f.close()
f=open("file2.txt",'r')
data2=f.read()
f.close()
data3=data1+data2
f=open("file3.txt",'w+')
f.write(data3)
f.seek(len(data1))
print(f.read())
print("\nTask completed:" )
f.close()



