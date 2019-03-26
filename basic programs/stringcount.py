string = input("Please enter a sentence: ")
count1=0
count2=0
count3=0
count4=0
for i in string:
    if(i.islower()):
        count1=count1+1
    elif(i.isupper()):
        count2=count2+1
    elif(i.isspace()):
        count3=count3+1
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i =='U':
        count4=count4+1
    
print("The number of lowercase")
print(count1)
print("The number of uppercase")
print(count2)
print("The number of space")
print(count3)
print("The number of vowel")
print(count4)

