class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        if k > n:
            return -1

        ans, slow, pre = 0, 0, -1

        for fast in range(n + k - 1):  # Ensure we check potential cycles
            cur = fast % n

            if colors[cur] == pre:  
                slow = cur  # Restart window
            elif fast - slow + 1 == k:  # Found valid sequence
                ans += 1
                slow += 1  # Move the window forward
            
            pre = colors[cur]

        return ans

# Test cases
soln = Solution()
print(soln.numberOfAlternatingGroups([0, 1, 0, 1, 0], 3))  # Output: 3
print(soln.numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6))  # Output: 2
print(soln.numberOfAlternatingGroups([1, 1, 0, 1], 4))  # Output: 0
print(soln.numberOfAlternatingGroups([0, 1, 0, 1], 3))  # Output: 0