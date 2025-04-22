MOD = 10**9 + 7
MAX_N=10**4 + 10
MAX_P=15 # Maximum 15 prime factors within 10**4
sieve = [0] * MAX_N # Prime factor

for i in range(2, MAX_N):
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i

# prime factors e.g. 12 = (2**2) * (3 ** 1), so ps[12] = [1, 2]
ps = [[] for _ in range(MAX_N)] 
for i in range(2, MAX_N):
    x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)

c = [[0] *(MAX_P + 1) for _ in range(MAX_N + MAX_P)]
# Classic Pascal Triangle for combination problem
c[0][0] = 1
# we have total of MAX_N array position, and MAX_P prime factor positions
# so in total, we have MAX_N + MAX_P positions to fill or arrange. 
# e.g. [1, 2, 2, 4]
#         ^  ^  ^
#         |  |  |
#         2     2
# this is C(6, 2)
for i in range(1, MAX_N + MAX_P):
    c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        '''
        We  use multiplications here because we can "squeeze" prime factors in between items
        in the SAME position. Therefore they do not care where other factors sit. Therefore
        independent, therefore multiplications.
        '''
        ans = 0
        for x in range(1, maxValue + 1):
            mul = 1
            for p in ps[x]:
                mul = mul * c[n + p - 1][p] % MOD
            ans = (ans + mul) % MOD
        return ans
    
    def idealArraysII(self, n: int, maxValue: int) -> int:
        '''
        TLE solution
        '''
        MOD = 1_000_000_007
        memo = [[0 for _ in range(maxValue + 1)] for _ in range(n)]
        def dfs(cur: int, pre:int) -> int:
            if cur == n or pre * 2 > maxValue:
                return 1
            if memo[cur][pre] > 0 :
                return memo[cur][pre]
            ans = 0
            for i in range(pre, maxValue + 1, pre):
                ans += dfs(cur + 1, i)
                ans %= MOD
            memo[cur][pre] = ans
            return ans

        ret = dfs(0, 1)
        return ret

soln = Solution()
print(soln.idealArrays(2, 5))
print(soln.idealArrays(5, 3))
print(soln.idealArrays(5, 9))            
