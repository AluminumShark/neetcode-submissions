# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        heights = {}
        
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                lh = heights.get(node.left, 0)
                rh = heights.get(node.right, 0)

                if abs(lh - rh) > 1:
                    return False
                
                heights[node] = 1 + max(lh, rh)

                if node.left in heights:
                    del node.left
                if node.right in heights:
                    del node.right

        return True