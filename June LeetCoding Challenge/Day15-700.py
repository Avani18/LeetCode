# Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/
'''Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.'''


def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val>val:
                curr=curr.left
            else:
                curr = curr.right
        return None
