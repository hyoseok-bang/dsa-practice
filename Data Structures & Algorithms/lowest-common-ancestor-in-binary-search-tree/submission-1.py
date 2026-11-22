# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# LCA 조건
# 1. 방문한 node의 값이 p와 q 사이인 경우 -> 그 node가 LCA
# 2. 방문한 node의 값이 p 또는 q와 같은 경우 -> 그 node가 LCA
# 탐색 조건
# - 방문한 node의 값이 p, q보다 큰 경우: left subtree 탐색
# - 방문한 node의 값이 p, q보다 작은 경우: right subtree 탐색

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        if root.val > min(p.val, q.val) and root.val < max(p.val, q.val):
            return root
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)