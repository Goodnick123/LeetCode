# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 18:57
# @Author  : Yeh
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """


demo =Solution()
from BuildTree import binaryTree
tree =binaryTree()
arr=[3,5,1,6,2,0,8,None,None,7,4]
root =tree.build(arr)
print(demo.lowestCommonAncestor(root,TreeNode(6),TreeNode(8)))