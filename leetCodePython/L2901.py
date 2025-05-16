from collections import deque
from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        dp = [1] * N
        pre = [-1] * N
        max_idx = 0
        max_len = 1
        dp[0] = 1
        for i in range(1, N):           
            for j in range(i):
                if self.hamming(words[j], words[i]) and groups[j] != groups[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        
        j = max_idx
        res = deque()
        while j >= 0:
            res.appendleft(words[j])
            j = pre[j]
        return list(res)
            
    def hamming(self, w1:str, w2:str) -> bool:
        if len(w1) != len(w2):
            return False
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        return diff == 1
    
soln = Solution()
print(soln.getWordsInLongestSubsequence(["bab","dab","cab"],  [1,2,2]))
print(soln.getWordsInLongestSubsequence(["a","b","c","d"],  [1,2,3,4]))
print(soln.getWordsInLongestSubsequence(["bdb","aaa","ada"], [2,1,3]))