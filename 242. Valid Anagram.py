s = 'aacc'
t = 'ccac'
# t ban sakta hai s me

arr1 = []
arr2 = []
final = []

for i in range(len(s)):
    arr1.append(s[i])

for j in range(len(t)):
    arr2.append(t[j])
    if t[j] in arr1:
        final.insert(j, t[j])
        arr1.remove(t[j])   # important fix
    else:
        pass

if len(s) == len(t) and final == arr2:
    print("true")
else:
    print("false")
