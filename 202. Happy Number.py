class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        for k in range(20) :
            snum = str(num)
            sum1= 0
            
            for i in range(len(snum)):
                sum1 += int(snum[i])**2
                
            if sum1 == 1:
                return True
                break
            elif k == 19:
                return False
                break
            else:
                num = sum1
