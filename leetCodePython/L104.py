# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if (root is None):
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

testTree = TreeNode(3)
testTree.left = TreeNode(9)
testTree.right = TreeNode(20)
testTree.right.left = TreeNode(15)
testTree.right.right = TreeNode(7)
soln = Solution()
print(soln.maxDepth(testTree))