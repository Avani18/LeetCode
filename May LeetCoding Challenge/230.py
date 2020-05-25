# Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.'''

def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
            
#This will run only in the Leetcode compiler because of the TreeNode class in that
