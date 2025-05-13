
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # dp[i][0] = number of 'a' after i iterations
        mod = 10 ** 9 + 7
        dp = [0] * 26
        for c in s:
            dp[ord(c) - ord('a')] += 1
        
        for i in range(t):
            temp = [0] * 26
            temp[0] = dp[25]
            temp[1] = (dp[0] + dp[25]) % mod
            for j in range(2, 26):
                temp[j] = dp[j - 1]
            dp = temp 
        ans = 0
        for i in range(26):
            ans = (ans + dp[i]) % mod
        return ans

soln = Solution()
print(soln.lengthAfterTransformations("abcyy", 2))
print(soln.lengthAfterTransformations("azbk", 1))