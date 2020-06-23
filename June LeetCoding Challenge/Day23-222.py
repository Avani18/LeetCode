# Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
'''Given a complete binary tree, count the number of nodes.'''


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.get_count(root)[1]

    def get_count(self, root, root_count=1):
        # print(f"root_count: {root_count}, {root.val}")
        left_cur, right_cur = root, root
        left_corner, right_corner = root_count, root_count
        while left_cur.left:
            left_cur = left_cur.left
            left_corner = left_corner * 2
        while right_cur.right:
            right_cur = right_cur.right
            right_corner = right_corner * 2 + 1
        if left_corner <= right_corner:
            return (True, right_corner)
        left_full_tree, left_count = self.get_count(root.left, root_count * 2)
        if not left_full_tree:
            return (False, left_count)
        if root.right:
            right_full_tree, right_count = self.get_count(
                root.right, root_count * 2 + 1
            )
            if not right_full_tree:
                return (False, right_count)
        return (False, left_count)
