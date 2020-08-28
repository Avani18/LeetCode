# Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
'''Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.'''

def bstFromPreorder(preorder):        
	return makeBST(preorder)
        
        
def makeBST(pre):
    
    stack = []
    root = TreeNode(pre[0])
    stack.append(root)
    i = 1
    
    while (i < len(pre)):
        temp = None
        while (len(stack) > 0 and pre[i] > stack[-1].val):
            temp = stack.pop()
            
        if (temp != None):
            temp.right = TreeNode(pre[i])
            stack.append(temp.right)
            
        else:
            temp = stack[-1]
            temp.left = TreeNode(pre[i])
            stack.append(temp.left)
            
        i += 1
        
    return root
    
#This function will work only in the Leetcode compiler as the Node class is defined there itself
