# -*- coding: utf-8 -*-
# @Time    : 2018/2/13 10:36
# @Author  : Yeh

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        res=[]
        while stack!=[] or root is not None:
            while root is not None:
                stack.append(root)
                root =root.left
            tmp =stack[-1]
            res.append(tmp.val)
            del stack[-1]
            if tmp.right is not None:
                root =tmp.right
        return res

demo =Solution()
root =TreeNode(1)
node1 =TreeNode(2)
node2 =TreeNode(3)
root.right =node1
node1.left=node2
print(demo.inorderTraversal(root))