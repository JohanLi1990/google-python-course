class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = [0] * 501
        for num in nums:
            arr[num] += 1
        for num in arr:
            if num % 2 == 1:
                return False
        return True