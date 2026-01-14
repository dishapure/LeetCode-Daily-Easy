# j >= i 
numarr = [1,2,3,4,5]
target = 6
for i in range(len(numarr)):
    for j in range(i+1,len(numarr)):
        if(numarr[i]+numarr[j]==target):
            print("["+str(i)+","+str(j)+"]")
