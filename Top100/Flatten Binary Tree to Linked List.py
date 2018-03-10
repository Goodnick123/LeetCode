# -*- coding: utf-8 -*-
# @Time    : 2018/2/18 10:53
# @Author  : Yeh

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def flatten(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: void Do not return anything,
    #     """
    #     stack=[]
    #     while stack!=[] or root !=None:
    #         while root !=None:
    #             stack.append(root)
    #             root =root.left
    #         tmp =stack[-1]
    #         del stack[-1]
    #         if tmp.left !=None:
    #             left = tmp.left
    #             tmp.left =None
    #             tmp.right =left
    #         if tmp.right !=None:
    #             root =tmp.right
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything,
        """
        if root !=None:
            if root.left !=None:
                self.flatten(root.left)
            if root.right !=None:
                self.flatten(root.right)
            tmp =root.right
            root.right =root.left
            root.left =None
            while root.right !=None:
                root =root.right
            root.right =tmp
from BuildTree import binaryTree

tree = binaryTree()
arr =[1,2,5,3,4,None,6]
root =tree.build(arr)
demo =Solution()
demo.flatten(root)
print(tree.inorderTraversal(root))

