# Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
''' Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        right = (self.invertTree(root.right))
        left = (self.invertTree(root.left))
        root.left = right
        root.right = left
        return root
