class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1) : return 1
        if (n == 2) : return 5
        acc = 5
        for i in range(2, n):
            acc += 4 + (i - 1) * 4
        return acc
    
    def standardSoln(self, n):
        return n**2 + (n - 1)**2
    
soln = Solution()
print(soln.coloredCells(5))
print(soln.standardSoln(5))
