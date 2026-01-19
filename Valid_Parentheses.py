o = ['(','{','[']
c = [')','}',']']
open = []
close = []


ip = "([)"

valid = True
arr2 = []

for i in range(len(ip)):
    arr2 += ip[i]
    current = ip[i]
    if current in o:
        open.append(current)
    else:
        close.append(current)
        

        last_open = open[-1]

        if o.index(last_open) == c.index(current):
            open.pop()
        else:
            valid = False
            break

if valid and len(open) == 0:
    print(True)
else:
    print(False)
