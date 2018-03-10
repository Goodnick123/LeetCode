# -*- coding: utf-8 -*-
# @Time    : 2018/2/22 9:58
# @Author  : Yeh


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    maxValue=-100000
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root== None:
            return 0
        self.pathDown(root)
        return self.maxValue
    def pathDown(self,root):
        if root == None:
            return 0
        left =max(0,self.pathDown(root.left))
        right =max(0,self.pathDown(root.right))
        self.maxValue =max(self.maxValue,left+right+root.val)
        return max(left,right)+root.val
from BuildTree import binaryTree
arr =[-3]
tree =binaryTree()
root =tree.build(arr)
demo = Solution()
print(demo.maxPathSum(root))