num = str(10); # converted to string

arr1 = [];
for i in range(len(num)): # len = 2
    arr1 += num[i]
    #arr1 = ["1","0"]
print(arr1)

arr2 = []
for i in range(len(arr1),0,-1): # 2
    arr2 += arr1[i-1]; # arr2 += 1, 
print(arr2)

if(arr1 == arr2):
    print(num+" is palindrome number")
else:
    print(num+" is not palindrome number")
