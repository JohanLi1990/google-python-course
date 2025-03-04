from collections import deque

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        q = deque()
        last = -1
        for i in range(0, len(nums)):
            if(nums[i] == val):
                q.append(i)
            elif len(q) > 0:
                cur = q.popleft()
                nums[cur] = nums[i]
                q.append(i)
                last = max(last, cur + 1)
            else:
                last = i + 1
        if (last == -1 and len(q) > 0) :
            nums = []
            return 0
        if (last == -1 and len(q) == 0):
            return len(nums)
        return last


if __name__ == "__main__":
    soln = Solution()
    test = [3,2,2,3]
    print(soln.removeElement([3,2,2,3], 3))
    test = [4, 5]
    print(soln.removeElement(test, 5))