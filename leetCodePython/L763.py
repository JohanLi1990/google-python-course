from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # for each letter find its last appearance
        
        lastSeen = {}
        for i, letter in enumerate(s):
            lastSeen[letter] = i
        
        ans = []
        prev = -1
        end = lastSeen[s[0]]
        for i in range(len(s)):
            end = max(end, lastSeen[s[i]])
            if i == end:
                ans.append(i - prev)
                prev = i
        return ans
    
soln = Solution()
print(soln.partitionLabels( "ababcbacadefegdehijhklij"))
print(soln.partitionLabels( "eccbbbbdec"))