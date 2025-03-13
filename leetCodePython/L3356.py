class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        1536ms
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        
        """
        def createDiff(index):
            arr = [0 for i in range(len(nums) + 1)]
            for i in range(0, index + 1):
                curQ = queries[i]
                arr[curQ[0]] -= curQ[2]
                arr[curQ[1] + 1] += curQ[2]
            return arr
        
        def isAllZero(diff):
            cur = 0
            for i in range(len(nums)):
                cur += diff[i]
                if nums[i] + cur > 0:
                    return False
            
            return True
        
        if isAllZero([0] * len(nums)):
            return 0
            
        l , r = 0, len(queries) - 1
        while(l < r):
            mid =l + (r - l)//2
            diff = createDiff(mid)
            if isAllZero(diff):
                r = mid
            else:
                l = mid + 1
        if isAllZero(createDiff(l)):
            return l + 1
        else:
            return -1
    
    def minZeroArrayII(self, nums, queries):
        """
        128ms implemntion
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int

        A naive approach yields O(mn) complexity

        sorting queries? Yes, but keep the index?
        see: https://leetcode.com/problems/zero-array-transformation-i/description/

        1/31
        """
        # Code sample (fastest)
        n = len(nums)
        p_sum = [0]*(n+1)
        s = 0
        k = 0

        # si = sum of ith until k queries 
        for i in range(n):
            s += p_sum[i]
            while s < nums[i]:
                if k == len(queries):
                    return -1
                l,r,v = queries[k]
                p_sum[l] += v
                p_sum[r+1] -= v
                if l<= i and i<= r:
                    s += v
                k += 1
        return k
        
soln = Solution()
print(soln.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]])) #2
print(soln.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]])) #-1
print(soln.minZeroArray([7,6,8], [[0,0,2],[0,1,5],[2,2,5],[0,2,4]])) #4
print(soln.minZeroArray([0], [[0,0,2],[0,1,5],[2,2,5],[0,2,4]])) #0