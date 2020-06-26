# Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.'''


def sumNumbers(self, root: TreeNode, sumToNode = 0) -> int:
        ans=0
        if root!=None:
            if root.left==None and root.right==None:
                return sumToNode*10 + root.val
            if root.left!=None:
                ans+=self.sumNumbers(root.left,sumToNode*10+root.val)
            if root.right!=None:
                ans+=self.sumNumbers(root.right,sumToNode*10+root.val)
        return ans
