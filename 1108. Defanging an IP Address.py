address = "255.100.50.0"

#"255[.]100[.]50[.]0"

words = list(address)
res = []

for i in range(len(words)):
    if words[i] == ".":
        res.append("[.]")
    else:
        res.append(words[i])

nres = ''.join(res)
print(nres)

