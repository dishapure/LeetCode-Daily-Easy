arr = [0,1,2,2,3,0,4,2]

val = 2

for i in range(len(arr)): #3
    current = arr[i]
    if current is val:
        arr.remove(current)
        arr.append("_")

print(arr)
