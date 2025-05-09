from functools import cache
from math import comb
from typing import Counter

class Solution:
# TODO: worth doing again sometime:https://leetcode.com/problems/count-number-of-balanced-permutations/description    
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        tot, n = 0, len(num)
        cnt = [0] * 10
        for ch in num:
            d = int(ch)
            cnt[d] += 1
            tot += d
        if tot % 2 == 1:
            return 0
        
        target = tot // 2
        max_odd = (n + 1) // 2
        f = [[0] * (max_odd + 1) for _ in range(target + 1)]
        f[0][0] = 1
        psum = tot_sum = 0
        # f[i][curr][odd_cnt]
        for i in range(10):
            # Sum of the number of the fir i digits:
            psum += cnt[i]
            # Sum of the first i  numbers
            tot_sum += i * cnt[i]
            for odd_cnt in range(min(psum, max_odd), max(0, psum - (n - max_odd)) - 1, -1):
                even_cnt = psum - odd_cnt
                for curr in range(min(tot_sum, target), max(0, tot_sum - target) -1 , -1):
                    res = 0
                    for j in range(max(0, cnt[i] - even_cnt), min(cnt[i], odd_cnt) + 1):
                        if i * j > curr:
                            break
                        ways = comb(odd_cnt, j) * comb(even_cnt, cnt[i] - j) % MOD
                        res = (res + ways * f[curr - i * j][odd_cnt - j] % MOD ) % MOD
                    f[curr][odd_cnt] = res % MOD
        return f[target][max_odd]
    
    def countBalancedPermutationsII(self, num: str) -> int:
        cnt = Counter(int(ch) for ch in num)
        total = sum(int(ch) for ch in num)

        @cache
        def dfs(i, odd, even, balance):
            if odd == 0 and even == 0 and balance == 0:
                return 1
            if i < 0 or odd < 0 or even < 0 or balance < 0:
                return 0
            res = 0
            for j in range(0, cnt[i] + 1):
                res += comb(odd, j) * comb(even, cnt[i] - j) * dfs(i - 1, odd - j, even - cnt[i] + j, balance - i * j)
            return res % 1000000007

        return 0 if total % 2 else dfs(9, len(num) - len(num) // 2, len(num) // 2, total // 2)

soln = Solution()
print(soln.countBalancedPermutationsII("123"))
            
            
                