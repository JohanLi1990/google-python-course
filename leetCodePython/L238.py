class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = []
        # right = []
        leftAcc = 1
        rightAcc = 1
        for i in range(len(nums)):
            left.append(leftAcc)
            leftAcc *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            left[i] *= rightAcc
            rightAcc *= nums[i]
        
        print(left)
        return left
    
soln = Solution()
soln.productExceptSelf([1, 2, 3, 4])
soln.productExceptSelf([-1,1,0,-3,3])