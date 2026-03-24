# 트리 - Binary Tree Maximum Path Sum
# 문제 링크: https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, maxi):
            if node is None:
                return 0, maxi

            val_left, maxL = dfs(node.left, maxi)
            val_right, maxR = dfs(node.right, maxi)

            val_left = max(val_left, 0)
            val_right = max(val_right, 0)

            # 현재 노드를 가운데로 하는 전체 경로
            cur = node.val + val_left + val_right
            maxi = max(maxi, maxL, maxR, cur)

            # 부모에게 넘길 값은 한쪽만
            ret = node.val + max(val_left, val_right)

            return ret, maxi

        return dfs(root, float('-inf'))[1]