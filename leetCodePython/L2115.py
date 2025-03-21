from collections import deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        inDegree={}
        for i, ingredient in enumerate(ingredients):
            for stuff in ingredient:
                graph[stuff] = graph.get(stuff, [])
                graph[stuff].append(recipes[i])
            inDegree[recipes[i]] = len(ingredient)
        # print(graph)
        # print(inDegree)
        
        queue = deque()
        for sup in supplies:
            queue.append(sup)
        
        ans = []
        while(len(queue) != 0):
            cur = queue.popleft()
            if cur not in graph:
                continue
            for child in graph[cur]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    ans.append(child)    
                    queue.append(child)
        return ans
        

soln = Solution()
print(soln.findAllRecipes( ["bread"], [["yeast","flour"]], ["yeast","flour","corn"]))
print(soln.findAllRecipes( ["bread","sandwich"],[["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]))     
print(soln.findAllRecipes( ["bread","sandwich", "burger"],[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]))
print(soln.findAllRecipes(
    ["ju","fzjnm","x","e","zpmcz","h","q"],
    [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]],
    ["f","hveml","cpivl","d"]
))
    
