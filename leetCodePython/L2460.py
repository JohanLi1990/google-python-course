class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = 0
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums[i], nums[i + 1] = 2 * nums[i], 0
            if nums[i] != 0 :
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return nums


if __name__ == '__main__':
    soln = Solution()
    print(soln.applyOperations([1,2,2,1,1,0 ]))
    print(soln.applyOperations([1,0]))
    print(soln.applyOperations([0,1]))