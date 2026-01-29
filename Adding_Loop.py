num = 38
res = 0

snum = str(num) # "38"

while res < 10: #0
    for i in range(len(snum)): # 2
        res = res +int(snum[i])
    snum = res
    

print(res)
