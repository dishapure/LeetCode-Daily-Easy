nums = [1,3,5,7]
res = 0

for i in range(len(nums)):
    if i%2 == 0:
        res = res + nums[i] #1-5-> -4
    else:
        res = res - nums[i] #4+(-4) -> 4-4

print(res)
