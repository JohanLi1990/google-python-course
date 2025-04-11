class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        def calculate(s:str) -> int:
            count = 0
            for c in s:
                count += int(c)
            return count
                    
        for i in range(low, high + 1, 1):
            cur_str = str(i)
            if len(cur_str) % 2 == 1:
                continue
                        
            first_half = cur_str[:len(cur_str) // 2]
            second_half = cur_str[len(cur_str) // 2 :]
            if calculate(first_half) == calculate(second_half):
                ans += 1
        return ans
    
soln = Solution()
print(soln.countSymmetricIntegers(1, 100)) # 9
print(soln.countSymmetricIntegers(1200, 1230)) # 4
            
            