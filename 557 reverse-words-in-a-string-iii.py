s = "Let's take LeetCode contest"
res = []

words = s.split(" ")

for i in range(len(words)):
    temp = ""
    for j in range(len(words[i])-1,-1,-1):
        temp += words[i][j]
    res.append(temp)

        
        
separator = ' '
my_string = separator.join(res)

print(my_string)
        
