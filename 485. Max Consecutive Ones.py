nums = [1,0,1,1,0,1]

c1 = 0
c2 = 0

for ch in nums:
    if ch == 1:
        c1 += 1
    else:
        c2 = max(c2, c1)
        c1 = 0

c2 = max(c2, c1)

print(c2)
