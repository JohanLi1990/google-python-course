class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isABC(c):
            return c in ['a', 'b', 'c']
        l = 0
        dict = {}
        ans = 0
        N = len(s)
        for r in range(N):
            if isABC(s[r]):
                dict[s[r]] = dict.get(s[r], 0) + 1
            while len(dict.keys()) == 3:
                ans +=  N - r
                dict[s[l]] -= 1
                if dict[s[l]] == 0:
                    dict.pop(s[l])
                l += 1
                
        return ans
    
soln = Solution()
print(soln.numberOfSubstrings( "abcabc")) #10
print(soln.numberOfSubstrings( "aaacb")) #3
                        