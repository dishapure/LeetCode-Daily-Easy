class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        resX = format(x, 'b')
        resY = format(y, 'b')

        if len(resX) > len(resY):
            diff = len(resX) - len(resY)
            resY = ('0' * diff) + resY

        elif len(resX) < len(resY):
            diff = len(resY) - len(resX)
            resX = ('0' * diff) + resX

        count = 0
        for i in range(len(resX)):
            if resX[i] != resY[i]:
                count += 1

        return count
