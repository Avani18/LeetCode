# Cousins in Binary Tree
# https://leetcode.com/problems/cousins-in-binary-tree/
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1. Two nodes of a binary tree are cousins if they have the same depth, but have different parents. We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree. Return true if and only if the nodes corresponding to the values x and y are cousins.

def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        self.xDepth = -1
        self.yDepth = -2
        self.xParent = None
        self.yParent = None

        def dfs(root, parent, x, y, depth):
            if root is None: return
            if root.val == x:
                self.xParent = parent
                self.xDepth = depth
            elif root.val == y:
                self.yParent = parent
                self.yDepth = depth
            else:
                dfs(root.left, root, x, y, depth+1)
                dfs(root.right, root, x, y, depth+1)

        dfs(root, None, x, y, 0)
        return self.xDepth == self.yDepth and self.xParent != self.yParent
        
#This will run only in the Leetcode compiler because of the Binary Tree class in that
