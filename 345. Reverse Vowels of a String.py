s = "IceCreAm"
 
vowels = ["A","E","I","O","U","a","e","i","o","u"]
v = []
res = []

for ch in s:
    if ch in vowels:
        v.append(ch)

vuno = v[::-1]

print(vuno)

j = 0
for ch in s:
    if ch in vowels and j <= len(vuno):
        res.append(vuno[j])
        j = j+1
    else:
        res.append(ch)
        
result = ''.join(res)

print(result)
        

