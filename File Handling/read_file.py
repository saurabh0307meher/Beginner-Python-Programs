file = open("abc.txt","w")

file.write("Hello\n")
file.write("This is saurabh\n")
file.close()

file = open("abc.txt","r")
read = file.readlines()
n = int(input("Enter which line to read"))
print(read[n-1])

