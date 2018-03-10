# -*- coding: utf-8 -*-
# @Time    : 2018/2/13 10:50
# @Author  : Yeh
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class binaryTree:
    #非递归
    def build(self,arr):
        queue=[]
        root =TreeNode(arr[0])
        queue.append(root)
        index = 1
        while index < len(arr):
            tmp =queue[0]
            del queue[0]
            if arr[index] !=None:
                node1 =TreeNode(arr[index])
                tmp.left =node1
                queue.append(node1)
            index+=1
            if index<len(arr):
                if arr[index]!=None:
                    node =TreeNode(arr[index])
                    tmp.right =node
                    queue.append(node)
                index+=1

        return root
    #中序
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while stack != [] or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            tmp = stack[-1]
            res.append(tmp.val)
            del stack[-1]
            if tmp.right is not None:
                root = tmp.right
        return res
# arr=[1,None,2,3]
# demo = binaryTree()
# root =demo.build(arr)
# print(root.val)
# print(demo.inorderTraversal(root))






