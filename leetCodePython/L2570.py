class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        p1, p2 = 0, 0
        while(p1 < len(nums1) and p2 < len(nums2)):
            if nums1[p1][0] < nums2[p2][0]:
                ans.append(nums1[p1])
                p1 += 1
            elif nums1[p1][0] > nums2[p2][0]:
                ans.append(nums2[p2])
                p2 += 1
            else:
                ans.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1
        ans.extend(nums1[p1:])
        ans.extend(nums2[p2:])
        return ans
    
if __name__ == '__main__':
    soln = Solution()
    print(soln.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
    print(soln.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))
    