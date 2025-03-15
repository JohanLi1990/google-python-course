class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return min(nums)
        l, r= 1, max(nums)
        while(l < r):
            mid = l + (r - l)//2
            curHomes = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    curHomes += 1
                    i += 2
                else:
                    i += 1
                if curHomes >= k:
                    break
                
            if curHomes >= k:
                r = mid
            else:
                l = mid + 1
        return l
    
soln = Solution()
print(soln.minCapability([2,3,5,9], 2))
print(soln.minCapability([2,7,9,3,1], 2))