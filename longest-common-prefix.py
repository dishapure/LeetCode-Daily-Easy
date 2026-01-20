arr = ["car", "cat", "ca"]

prefix = ""

for i in range(len(arr[0])): #car, cat
    current_char = arr[0][i] #c, c
    
    for word in arr: #car
        if word[i] != current_char: #word[i] = car[0] = c
            print(prefix)
            exit()
    prefix += current_char
print(prefix)
