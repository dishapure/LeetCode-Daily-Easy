class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sec = []

        for x in nums[:]:   # copy
            if x == 0:
                nums.remove(x)
                sec.append(0)

        res = nums.extend(sec)
        return res      
