class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2      # skip the pair
            else:
                return nums[i]
        return nums[i]       # handles single at the end
