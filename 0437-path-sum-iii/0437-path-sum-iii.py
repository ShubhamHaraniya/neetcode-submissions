# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def countPaths(node, target):
            if not node:
                return 0

            res = 0
            if node.val == target:
                res += 1

            res += countPaths(node.left, target - node.val)
            res += countPaths(node.right, target - node.val)

            return res

        if not root:
            return 0

        return (
            countPaths(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )