class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        arr2 = [] # [1, 2, 3, 4, 5, 6, 7, 8]
        final = []

        for i in range(1,len(nums)+1):
            arr2.append(i)


        for j in range(0,len(arr2)):
            current = arr2[j]
            if current in nums:
                pass
            else:
                final.append(arr2[j])

        return final
    
    
        
