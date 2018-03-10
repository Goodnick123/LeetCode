# -*- coding: utf-8 -*-
# @Time    : 2018/2/17 23:25
# @Author  : Yeh

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:


    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return []
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if inStart > inEnd or preStart > preEnd:
            return None
        node = TreeNode(preorder[preStart])
        index = 0
        for i in range(inStart, inEnd + 1):
            if preorder[preStart] == inorder[i]:
                index = i
                break
        leftLength = index - inStart
        node.left = self.build(preorder, preStart + 1, preStart + leftLength, inorder, inStart, index - 1)
        node.right = self.build(preorder, preStart + leftLength + 1, preEnd, inorder, index + 1, inEnd)
        return node

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
demo = Solution()
root =demo.buildTree(preorder,inorder)
from BuildTree import binaryTree
tree =binaryTree()
print(tree.inorderTraversal(root))
