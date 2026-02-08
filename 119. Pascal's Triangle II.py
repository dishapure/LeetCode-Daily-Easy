class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        big = []
        num = rowIndex + 1

        for i in range(1, num + 1):
            small = []
            for j in range(0, i):
                if j == 0 or j == i - 1:
                    small.append(1)
                else:
                    a = big[-1]
                    small.append(a[j] + a[j - 1])
            big.append(small)

        return big[rowIndex]
