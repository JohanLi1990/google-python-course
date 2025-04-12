from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        '''
        Good integers are nothing but permutation of k-palindrome
        some permutations have leading zeros and cannot be permitted 

        515, 525, 535, 545, 555, 565, 575, 585. 595
        
        distinct permutation = n! / (k1! * k2! *... *kr!)
        where n = total number of elements
        and each ki is the count of how many times a particular repeated elements occur
             
        The gist is the formulae above, but the engineering is also important: how do you avoid double counting your palindrome?
        '''
        
        dict = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1 # very samrt here, odd will be 1, even will be zero
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            if int(s) % k == 0:
                dict.add("".join(sorted(s)))
        
        fact = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dict:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            total = (n - cnt[0]) * fact[n - 1]
            for x in cnt:
                total //= fact[x]
            ans += total
        return ans
    
soln = Solution()
print(soln.countGoodIntegers(3, 5)) #27
print(soln.countGoodIntegers(1, 4)) #2
print(soln.countGoodIntegers(5, 6)) #2468
        
        