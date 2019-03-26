import time 
file = open("testfile.txt","a")
for i in range(10):  
    file.write("\n Hello World!!!!!!!")
    time.sleep(1)
    print("wait for 10 seconds")
file.close()
    

