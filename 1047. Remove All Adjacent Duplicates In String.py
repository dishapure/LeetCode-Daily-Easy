s = "azxxzy"
s = list(s)


for i in range(len(s)-1,-1,-1):
    if s[i] == s[i-1]:
        s.remove(s[i])
        s.remove(s[i-1])
        
res = "".join(s)

print(res)
