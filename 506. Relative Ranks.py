score = [10,3,8,9,4]
res = [""] * len(score)
original = score[:]   # copy, not reference

score.sort(reverse=True) 

count = 1

for ch in score:
    idx = original.index(ch)   
    if count == 1:
        res[idx] = "Gold Medal"
    elif count == 2:
        res[idx] = "Silver Medal"
    elif count == 3:
        res[idx] = "Bronze Medal"
    else:
        res[idx] = str(count)

    count += 1
    
print(res)
    
