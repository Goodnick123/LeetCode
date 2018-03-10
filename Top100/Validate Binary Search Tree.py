# -*- coding: utf-8 -*-
# @Time    : 2018/2/13 17:07
# @Author  : Yeh

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from BuildTree import binaryTree
class Solution:
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     stack=[]
    #     if root==None:return True
    #     else:
    #         stack.append(root)
    #     while stack !=[]:
    #         tmp =stack[0]
    #         del stack[0]
    #         if tmp.left !=None:
    #             if tmp.left.val<tmp.val:
    #                 stack.append(tmp.left)
    #             else:
    #                 return False
    #         if tmp.right!=None:
    #             if tmp.right.val>tmp.val:
    #                 stack.append(tmp.right)
    #             else:
    #                 return False
    #     return True
    def isValidBST(self, root):
        stack =[]
        res=[]
        while stack!=[] or root!=None:
            while root !=None:
                stack.append(root)
                root =root.left
            tmp =stack[-1]
            del stack[-1]
            res.append(tmp.val)
            if tmp.right is not None:
                root =tmp.right
        for i in range(1,len(res)):
            if res[i-1]>=res[i]:
                return False
        return True


tree =binaryTree()
arr=[3,2,4,1,None,None,6]
root =tree.build(arr)
demo =Solution()
print(demo.isValidBST(root))

        