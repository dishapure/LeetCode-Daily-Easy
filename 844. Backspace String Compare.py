s = list("ab##")
t = list("c#d#")

for i in s:
    if i == "#":
        num = s.index('#')
        print("removing", num,"and #")
        s.pop(num-1)
        s.remove("#")
        print(s, "i=",i)
        

for j in t:
    if j == "#":
        num = t.index('#')
        t.pop(num-1)
        t.remove("#")

    

if s == t:
    print("true")
else:
    print("false")
