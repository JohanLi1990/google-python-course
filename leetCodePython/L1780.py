class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3**15 larger then 10**7
        # return self.dfs(0, n)
        return self.correctSoln(n)
    
    def dfs(self, power, target):
        '''
        power: int
        target: left over
        '''
        if target == 0:
            return True
        if target < 0:
            return False
        if power > 15:
            return False
        
        return self.dfs(power + 1, target - 3**power) or self.dfs(power + 1, target)
    
    def correctSoln(self, n):
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

soln = Solution()
print(soln.checkPowersOfThree(12))
print(soln.checkPowersOfThree(91))
print(soln.checkPowersOfThree(21))
print(soln.checkPowersOfThree(10**7))