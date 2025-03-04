class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        vol = 0
        while(l < r) :
            if height[l] < height[r]:
                vol = max(vol, height[l] * (r - l))
                l += 1
            else:
                vol = max(vol, height[r] * (r - l))
                r -= 1
        return vol

if __name__ == '__main__':
    soln = Solution()
    print(soln.maxArea([1,8,6,2,5,4,8,3,7]))