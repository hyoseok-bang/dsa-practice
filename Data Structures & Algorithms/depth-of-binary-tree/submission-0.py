# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # track depth of each node explicitly, unlike recursion
        
        stack = [[root, 1]]  # initialize stack with root node
        res = 0  # initalize maximum depth with 0; since the minimum depth is 1, the initial value of res should be less than or equal to 1
        while stack:  # iterate until the stack is empty
            node, depth = stack.pop()  # get the latest node and its depth
            if node:  # if the node is not null
                res = max(res, depth)  # update res with the max value between the current depth and the current max depth
                stack.append([node.left, depth + 1])  # add the left child node to stack, with an updated depth
                stack.append([node.right, depth + 1])  # add the right child node to stack, with an updated depth
        return res