class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = sorted(nums, reverse=True)

        final = []

        for x in res:
            if x not in final:
                final.append(x)
                
        try:
            return final[2]
        except IndexError:
            return max(final)

       
