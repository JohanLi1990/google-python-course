from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = {}
        res = 0
        for dom in dominoes:
            hashkey = dom[0] * 10 + dom[1] if dom[0] < dom[1] else dom[1] * 10 + dom[0]
            past = seen.get(hashkey, 0)
            res += past
            seen[hashkey] = past + 1
        return res

soln = Solution()
print(soln.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])) # 1
print(soln.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]])) # 3
