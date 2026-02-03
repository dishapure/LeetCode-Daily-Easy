class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inums = []

        for i in range(0,len(nums)+1):
            inums.append(i)
            if i in nums:
                pass
            else:
                return i      
                
