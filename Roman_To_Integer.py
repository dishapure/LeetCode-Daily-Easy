# Roman To Integer
r = "XIX"

romans = {
  "I": 1,
  "V": 5,
  "X": 10,
}

arr = []
total = 0;
for i in range(len(r)):
    arr += r[i]
    if i < len(arr) - 1:
        if romans[arr[i]] < romans[arr[i+1]]:
            total = total - romans[arr[i]]
        else:
            total = total + romans[arr[i]]
    else:
        # last character → always add
        total = total + romans[arr[i]]

print(total)
    
    

    
    


