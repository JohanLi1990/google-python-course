class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        #  count the number of choices from right to left
        
        def calculate(curstr: str) -> int:
            if len(curstr) < len(s):
                return 0
            if len(curstr) == len(s):
                return 1 if int(curstr) >= int(s) else 0
            
            count = 0
            prefix_len = len(curstr) - len(s)
            suffix = curstr[prefix_len:]
            for i in range(prefix_len):
                if int(curstr[i]) > limit:
                    count += (limit + 1)**(prefix_len - i)
                    return count
                count += int(curstr[i]) * (limit + 1)**(prefix_len - i - 1)
            
            if int(suffix) >= int(s):
                count += 1
            
            return count
        
        return calculate(str(finish)) - calculate(str(start - 1))
    
soln = Solution()
# print(soln.numberOfPowerfulInt(1, 6000, 4, "124"))
# print(soln.numberOfPowerfulInt(15, 215, 6, "10"))
# print(soln.numberOfPowerfulInt(1000, 2000, 4, "3000"))
# print(soln.numberOfPowerfulInt(15, 215, 6, "1"))
print(soln.numberOfPowerfulInt(1,971, 9, '72'))
            