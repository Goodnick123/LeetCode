# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 15:47
# @Author  : Yeh

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root !=None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            tmp =root.left
            root.left=root.right
            root.right =tmp
        return root

from BuildTree import binaryTree

demo =Solution()
arr=[1,2,3,4,5]
tree =binaryTree()
root =tree.build(arr)
print(tree.inorderTraversal(root))
t =demo.invertTree(root)
print(tree.inorderTraversal(t))