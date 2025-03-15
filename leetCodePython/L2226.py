class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if (len(candies) == 1):
            return sum(candies) // k
        max = sum(candies) // k
        if (max <= 1) : return max
        l, r = 0, max
        while l < r:
            mid = l + (r - l) // 2 + 1
            numChildren = 0
            for candy in candies:
                numChildren += candy // mid
                if (numChildren >= k):
                    break
            if numChildren < k:
                r = mid - 1
            else:
                l = mid
        return l
        
soln = Solution()
print(soln.maximumCandies([5,8,6], 3))
print(soln.maximumCandies([2,5], 11))
print(soln.maximumCandies([9,8,6,7], 6))
print(soln.maximumCandies([6], 6))
print(soln.maximumCandies([4,7,5], 16))