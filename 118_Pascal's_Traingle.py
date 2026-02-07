class Solution(object):
    def generate(self, numRows):

        big = []
        num = numRows
        
        for i in range(1,num+1):
            small = []
            for j in range(0,i): 
                
                if j == 0:
                    small.append(1)
                elif j == i-1:
                    small.append(1)
                else:
                    a = big[-1]
                    sum= a[j]+a[j-1]
                    small.append(sum)
            big.append(small)
            

        return big
