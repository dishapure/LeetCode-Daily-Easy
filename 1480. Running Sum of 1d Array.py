class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []

        for i in range(len(nums)): # 4
            temp = 0
            for j in range(i+1): # 0
                j = j+1
                temp += nums[j-1]
            res.append(temp)

        return res
