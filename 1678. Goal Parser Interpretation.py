command = "G()()()()(al)"
# "G" as the string "G", "()" as the string "o", and "(al)" as the string "al"

i = 0
res = ""

while i < len(command):
    if command[i] == 'G':
        res += 'G'
        i += 1
    elif command[i] == '(' and command[i+1] == ')':
        res += 'o'
        i += 2
    else:
        res += 'al'
        i += 4

print(res)
