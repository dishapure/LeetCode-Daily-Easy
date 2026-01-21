list1 = [0,5,9]
list2 = [1,2,3,4]
res = []

if len(list1) < len(list2): # l1 < l2
    diff = len(list2)-len(list1)
    for i in range(diff):
        list1.append("-")
elif len(list1) > len(list2):
    diff = len(list1)-len(list2)
    for i in range(diff):
        list2.append("-")

for i in range(len(list1)):
    current = list1[i]
    res.append(current)
    for j in range(len(list2)):
        res.append(list2[i])
        break;

print(list1)
print(list2)
print(res)

res.remove("-")
print("Sorted Array is.....")
print(res)        
