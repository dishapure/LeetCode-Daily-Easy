class Solution:
    def minimumOperations(self, nums):
        count = 0
        
        for x in nums:
            if x % 3 != 0:
                count += 1
                
        return count
