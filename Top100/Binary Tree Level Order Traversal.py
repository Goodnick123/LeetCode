# -*- coding: utf-8 -*-
# @Time    : 2018/2/17 18:37
# @Author  : Yeh


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from BuildTree import binaryTree
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        curNum =0;lstNum =1
        queue=[]
        res =[]
        queue.append(root)
        lst=[]
        while queue != []:
            tmp =queue[0]
            del queue[0]
            lst.append(tmp.val)
            if tmp.left!=None:
                queue.append(tmp.left)
            if tmp.right!=None:
                queue.append(tmp.right)
            curNum+=1
            if curNum==lstNum:
                curNum =0
                lstNum =len(queue)
                res.append(lst.copy())
                lst=[]
        return res
arr=[1,2,3,4,5]
tree =  binaryTree()
root =tree.build(arr)
demo = Solution()
print(demo.levelOrder(root))