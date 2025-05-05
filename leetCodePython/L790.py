class Solution:
    def numTilings(self, n: int) -> int:
        # f(k) = f(k - 1) + f(k - 2) + p(k - 1) * 2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        fully = [0] * (n + 1)
        partial = [0] * (n + 1)
        fully[1] = 1
        fully[2] = 2
        partial[2] = 1
        MOD = 1_000_000_007
        for i in range(3, n + 1):
            fully[i] = (fully[i - 1] + fully[i - 2] + partial[i - 1] * 2) % MOD
            partial[i] = (fully[i - 2] + partial[i - 1]) % MOD
        return fully[n]

soln = Solution()
print(soln.numTilings(3))
print(soln.numTilings(1))
