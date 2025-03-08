class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # select a subarray of k where num(W) is smallest
        # sliding windows
        
        slow = 0
        num_white = 0
        min_white = 1000
        for i in range(len(blocks)):
            if blocks[i] == 'W': 
                num_white += 1
            while (i - slow + 1 > k):
                if blocks[slow] == 'W':
                    num_white -= 1
                slow += 1
            if i - slow + 1 == k:
                # print(f"i is {i}, min_white is {min_white}")
                min_white = min(min_white, num_white)
        return min_white
    
soln = Solution()
soln.minimumRecolors("WBBWWBBWBW", 7)
soln.minimumRecolors("WBWBBBW", 2)