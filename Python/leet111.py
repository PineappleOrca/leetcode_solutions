from collections import deque
# Finding the minimum depth of a binary tree
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root])
        level = 0
        min_level = float("inf")
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                # checking if you are at a leaf node
                if not node.left and not node.right:
                    level += 1
                    return level
                # traversing the graph to find the first leaf node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
            min_level = min(level,min_level)