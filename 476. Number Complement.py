num = 5
nnum = list(bin(num)[2:])
res = []

for i in range(len(nnum)):
    res.append('0' if nnum[i] == '1' else '1')


y = ''.join(str(x) for x in res)
print(int(y,2))
