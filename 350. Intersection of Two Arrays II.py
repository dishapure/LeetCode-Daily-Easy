class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = nums1
        n2 = nums2
        res = []
        ind = []

        for num1 in n1:
            i = 0                  # counter starts
            for num2 in n2:
                if num1 == num2 and i not in ind:
                    res.append(num1)
                    ind.append(i)
                    break
                i += 1             # move index manually

        return res
