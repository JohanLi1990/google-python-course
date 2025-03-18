class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        cur = 0
        maxlen = 1
        for i in range(len(nums)):
            if nums[i] & cur == 0:
                cur += nums[i]
                maxlen = max(maxlen, i - j + 1)
                continue
            
            while (j < i) and (cur & nums[i] != 0):
                cur -= nums[j]
                j += 1
            
            cur = nums[j]
                
        return maxlen
    
soln = Solution()
# print(soln.longestNiceSubarray([1,3,8,48,10])) 
# print(soln.longestNiceSubarray([3,1,5,11,13])) 
print(soln.longestNiceSubarray([4, 3, 4, 3]))