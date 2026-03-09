class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ops = operations
        res = []

        for op in ops:
            if op == "+":
                res.append(res[-1] + res[-2])
            elif op == "D":
                res.append(2 * res[-1])
            elif op == "C":
                res.pop()
            else:
                res.append(int(op))

        return sum(res)
