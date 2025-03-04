class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        curNum = n
        while True:
            curAns = 0
            while curNum > 0:
                curAns += (curNum % 10)**2
                curNum //= 10
            if (curAns in seen): return False
            if (curAns == 1): return True
            seen.add(curAns)
            curNum = curAns
        
soln = Solution()
print(soln.isHappy(2**31 - 1))