# 트리, BFS - Binary Tree Level Order Traversal
# 문제 링크: https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        result = []
        if root is None:
            return result
        que = deque([[root]])
        while que:
            cur = que.popleft()
            vals = []            
            nxt = []
            for c in cur:
                vals.append(c.val)

                if c.left is not None:
                    nxt.append(c.left)

                if c.right is not None:
                    nxt.append(c.right)
            
            result.append(vals)
            if nxt: 
                que.append(nxt)
        
        return result