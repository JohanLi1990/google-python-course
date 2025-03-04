#!/usr/bin/python3
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # if go from front doesn't work, always consider going from the back
        p3 = m + n - 1
        p2 = n - 1
        p1 = m - 1
        if p2 < 0: return
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
            p3 -= 1
        
        while p1 >= 0:
            nums1[p3] = nums1[p1]
            p1 -= 1
            p3 -= 1
        
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1
        # print(nums1)
    
if __name__ == "__main__":
    soln = Solution()
    ans = [1,2,3,0,0,0]
    soln.merge(ans, 3, [2, 5, 6], 3)
    print(ans)
    test2 = [0]
    soln.merge(test2, 0, [1], 1)
    print(test2)