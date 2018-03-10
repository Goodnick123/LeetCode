# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 22:08
# @Author  : Yeh
from BuildTree import binaryTree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queue =[]
        lst =[]
        lst.append(root)
        queue.append(root)
        curNum =0;lstNum=1
        while queue !=[]:
            tmp =queue[0]
            del queue[0]
            del lst[0]
            if tmp.left!=None:
                queue.append(tmp.left)
                lst.append(tmp.left.val)
            elif tmp.val!=False and tmp.left ==None:
                queue.append(TreeNode(False))
                lst.append(False)
            if tmp.right !=None:
                queue.append(tmp.right)
                lst.append(tmp.right.val)
            elif tmp.val!=False and tmp.right == None:
                queue.append(TreeNode(False))
                lst.append(False)
            curNum+=1
            if curNum == lstNum:
                curNum=0
                lstNum =len(queue)
                if self.checkUp(lst) ==False:
                    return False
        return True

    def checkUp(self,arr):
        start =0
        end =len(arr)-1
        while start<end:
            if arr[start]!=arr[end]:
                return False
            start+=1
            end-=1
        return True

    def isSymmetric(self,root):
        return self.check(root,root)
    def check(self,x,y):
        if x==None and y==None:
            return True
        if (x==None and y!=None) or (x!=None and y==None):
            return False
        return x.val==y.val and self.check(x.left,y.right) and self.check(x.right,y.left)
tree =binaryTree()
arr=[1,2,2,3,4,4,3]
root =tree.build(arr)
demo =Solution()
print(demo.isSymmetric(root))


