ll = [1,1,2,3,3]
l2 = []

for i in range(len(ll)):
    if ll[i] in l2:
        pass
    else:
        l2.append(ll[i])

print(l2)
