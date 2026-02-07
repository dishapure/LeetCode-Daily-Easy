big = []
num = 5
for i in range(1,num+1):
    small = []
    for j in range(0,i): 
        
        if j == 0:
            small.append(1)
        elif j == i-1:
            small.append(1)
        else:
            small.append('-')
    big.append(small)
    

print(big)
