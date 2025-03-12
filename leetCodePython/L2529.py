class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def besearch(judge, drop, retain, decide):
            '''
            judge: fun, Predicate, what is the criteria of dropping half of list?
            drop: fun, which half to drop?
            retain: fun which half to retain?
            '''
            l , r = 0, len(nums) - 1
            while(l < r - 1):
                mid = l + (r - l) // 2
                if judge(nums[mid]):
                    l, r = drop(l, r, mid)
                else:
                    l, r = retain(l, r, mid)
            return decide(l, r)
        
        neg = besearch(lambda x: x >= 0, lambda l, r, mid: (l, mid - 1), lambda l, r, mid:(mid, r), 
                       lambda a, b: b if nums[b] < 0 else a if nums[a] < 0 else -1)
        pos = besearch(lambda x: x <= 0, lambda l, r, mid: (mid + 1, r), lambda l, r, mid:(l, mid), 
                       lambda a, b: a if nums[a] > 0 else b if nums[b] > 0 else -1)
        
        neg = 0 if neg == -1 else neg + 1
        pos = 0 if pos == -1 else len(nums) - pos
        return max(neg, pos)
    
    def maximumCountII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0]>0 or nums[-1]<0:
            return len(nums)
        n=len(nums)
        l,r=0,n-1
        while l<r:
            m=l+(r-l)//2
            if nums[m]<0:
                l=m+1
            else:
                r=m
        a=l
        l,r=0,n-1
        while l<r:
            m=r-(r-l)//2
            if nums[m]>0:
                r=m-1
            else:
                l=m
        b=r
        if a>n-b-1:
            return a
        else:
            return n-b-1
    
soln = Solution()
# print(soln.maximumCount([-2,-1,-1,1,2,3]))
print(soln.maximumCountII([-3,-2,-1,0,0,1,2]))
# print(soln.maximumCount([-1563,-236,-114,-55,427,447,687,752,1021,1636]))