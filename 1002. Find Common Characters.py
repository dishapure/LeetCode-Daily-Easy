strings = ["cool", "lock", "cook"]

result = []

for ch in strings[0]:          # c o o l
    found = True

    for s in strings[1:]:      # lock, cook
        if ch in s:            # YES
            found = True
        else:                  # ELSE
            found = False
            break

    if found:
        result.append(ch)

print(result)
