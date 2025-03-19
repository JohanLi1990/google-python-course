class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        def flip(index):
            '''
            index: Int
            ret: void
            '''
            if index + 1 >= len(nums) or index + 2 >= len(nums):
                return
            nums[index] = 1 - nums[index]
            nums[index + 1] = 1 - nums[index + 1]
            nums[index + 2] = 1 - nums[index + 2] 
            
        for i in range(len(nums)):
            if nums[i] == 0:
                flip(i)
                ans += 1
            if nums[i] == 0:
                return -1
        return ans

soln = Solution()
print(soln.minOperations([0,1,1,1,0,0]))
print(soln.minOperations([0,1,1,1]))