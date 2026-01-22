num = [0,0,1,1,1,2,2,3,3,4]
num2 = []
numLen = len(num)

for i in range(numLen):
    current = num[i]
    if current in num2:
        pass
    else:
        num2.append(current)

print(len(num2))

totalLen = len(num)-len(num2)
#print(totalLen)

for i in range(totalLen):
    num2.append("-")

print(num2)
    
