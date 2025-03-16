class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        l, r = 0, min(ranks) * int(cars ** 2)
        while l < r :
            mid = l + (r - l) // 2
            numCars = 0
            for rank in ranks:
                numCars += int((mid // rank) ** 0.5)
                if numCars >= cars:
                    break
            if numCars >= cars:
                r = mid
            else:
                l = mid + 1
        return l
    
soln = Solution()
print(soln.repairCars([4,2,3,1], 10))
print(soln.repairCars([5,1,8], 6))

        