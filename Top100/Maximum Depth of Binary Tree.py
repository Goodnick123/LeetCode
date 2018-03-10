# -*- coding: utf-8 -*-
# @Time    : 2018/2/17 22:52
# @Author  : Yeh

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from BuildTree import binaryTree
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root ==None:
            return 0;
        left =self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1

tree = binaryTree()
arr=[3,9,20,None,None,15,7]
root = tree.build(arr)
demo =Solution()
print(demo.maxDepth(root))

