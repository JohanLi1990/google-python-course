class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        N = right + 1
        prime_array = [True for i in range(N)]
        prime_array[0] = prime_array[1] = False
        for i in range(2, int(N**0.5) + 1):
            if prime_array[i]:
                for j in range(i*i, N, i):
                    prime_array[j] = False
                
        ans = [-1, -1]
        diff = 10**7
        prev = -1
        for i in range(left, right + 1):
            if prime_array[i]:
                if prev == -1:
                    prev = i
                elif i - prev < diff:
                    ans[0] = prev
                    ans[1] = i
                    diff = i - prev
                    prev = i 
        return ans

soln = Solution()
print(soln.closestPrimes(10, 19))
print(soln.closestPrimes(1, int(10**6)))             
print(soln.closestPrimes(19, 31))