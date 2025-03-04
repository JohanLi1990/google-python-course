from collections import deque
class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        qsmall = deque()
        qlarge = deque()
        numEqual = 0
        for num in nums:
            if (num < pivot):
                qsmall.append(num)
            elif num > pivot:
                qlarge.append(num) 
            else:
                numEqual += 1
        i = 0
        while len(qsmall) > 0:
            nums[i] = qsmall.popleft()
            i += 1
        while(numEqual > 0):
            nums[i] = pivot
            i += 1
            numEqual -= 1
        while len(qlarge) > 0:
            nums[i] = qlarge.popleft()
            i += 1
        return nums
    

soln = Solution()
print(soln.pivotArray([9,12,5,10,14,3,10], 10))
print(soln.pivotArray([-3,4,3,2], 2))