# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Tree의 level별로 가장 오른쪽에 있는 노드를 찾기
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            right_node = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    right_node = node
                    q.append(node.left)
                    q.append(node.right)
            if right_node:
                res.append(right_node.val)
        return res