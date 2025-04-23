class Solution:
    def countLargestGroup(self, n: int) -> int:
        arr=[0] * 37
        ans = -1
        res = 0
        for i in range(1, n + 1):
            curSum = 0
            x = i
            while x > 0:
                curSum += x % 10
                x //= 10
            arr[curSum] += 1
            ans = max(ans, arr[curSum])
        # print(arr)
        for i in range(37):
            if ans == arr[i]:
                res += 1
        return res

soln = Solution()
print(soln.countLargestGroup(13))
print(soln.countLargestGroup(2))