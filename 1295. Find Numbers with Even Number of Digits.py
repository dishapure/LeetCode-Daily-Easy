class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for i in range(len(nums)):
            curr = nums[i]
            li = list(nums)
            if len(str(curr)) % 2 == 0:
                res += 1
            else:
                pass

        return res
