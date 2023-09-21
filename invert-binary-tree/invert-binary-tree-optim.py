from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap
        root.left, root.right = root.right, root.left

        # Recursion
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

s = Solution()
print(s.invertTree([4,2,7,1,3,6,9]))
