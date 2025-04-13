class Solution:
    def countGoodNumbers(self, n: int) -> int:
        '''
        permutation and combinations
        when n = 4
            4 * 4 * 5 * 4
        '''
        mod = 1_000_000_007
        def mod_exp(a:int, n:int) -> int:
            result = 1
            a = a % mod
            while  n > 0:
                if n % 2 == 1:
                    result = (result * a) % mod
                a = (a * a) % mod
                n = n // 2
            return result
        
        if n % 2 == 0:
            return mod_exp(20, n // 2)
        else:
            return 5 * mod_exp(20, n // 2) % mod
        
    
soln = Solution()
print(soln.countGoodNumbers(1))
print(soln.countGoodNumbers(4))
print(soln.countGoodNumbers(50)) 