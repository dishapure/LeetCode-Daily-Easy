n1 = [4,9,5]
n2 = [9,4,9,8,4]
res = []

if len(n1) > len(n2):
    diff = len(n1) - len(n2)
    for i in range(diff):
        n2.append('_')

elif len(n1) < len(n2):
    diff = len(n2) - len(n1)
    for i in range(diff):
        n1.append('_')
    
for i in range(len(n1)):
    if n1[i] in n2 and n1[i] not in res:
        res.append(n1[i])

print(res)
