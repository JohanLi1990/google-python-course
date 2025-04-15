from typing import List

from sortedcontainers import SortedList
class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    
    def update(self, index: int, delta:int):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index
            
            
    def query(self, index:int) -> int:
        res = 0
        index += 1
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        pos2 = [0] * n
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        reversedIndex = [0] * n
        for i, num1 in enumerate(nums1):
            reversedIndex[pos2[num1]] = i
        res = 0
        fenwick = BIT(n)
        for j in range(n):
            pos = reversedIndex[j]
            left = fenwick.query(pos)
            fenwick.update(pos, 1)
            right = (n - 1 - pos) - (j - left)  # Need to find the number of values that are on the right of both nums1 and nums2
            res += left * right
        return res
    
    # Very very smart solution
    def goodTripletsII(self, nums1: List[int], nums2: List[int]) -> int:
        res, inds, arr = 0, [0]*len(nums1), SortedList()
        for i,num in enumerate(nums1):      
            inds[num] = i
            
        nonreversed = [0] * len(nums1)
        for i,num in enumerate(nums2):      
            nonreversed[i] = inds[num]
            
        reversedarr = nonreversed[::-1]
        # i refers to the number of items from the right of nums2
        # num refers to the postion of nums2[n - 1 - i] in nums1
        # ind = arr.bisect(num) find the number of items that are actually on the left of cur position in nums1. 
        # i - ind calculates the number of items that are both on the right of cur item. 
        for i,num in enumerate(reversedarr):
            ind = arr.bisect(num)
            res += (i-ind)*(num-ind) 
            arr.add(num)
        return res
    
soln = Solution()
# print(soln.goodTripletsII([2,0,1,3], [0,1,2,3]))
print(soln.goodTripletsII([4,0,1,3,2], [4,1,0,2,3]))