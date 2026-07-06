class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaves):
            if not root:
                return

            if not root.left and not root.right:
                leaves.append(root.val)
                return

            dfs(root.left, leaves)
            dfs(root.right, leaves)

        r1, r2 = [], []
        dfs(root1, r1)
        dfs(root2, r2)

        return r1 == r2