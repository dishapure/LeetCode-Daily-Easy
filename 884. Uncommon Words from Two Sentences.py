s1 = "apple apple"
s2 = "banana"

words = (s1 + " " + s2).split()
res = []

for w in words:
    if words.count(w) == 1:
        res.append(w)

print(res)
