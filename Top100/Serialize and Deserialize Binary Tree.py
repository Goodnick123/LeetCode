# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 22:59
# @Author  : Yeh


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root==None:return "[null]"
        res=[]
        queue=[]
        queue.append(root)
        res.append(str(root.val))
        cnt,last,level=0,1,0
        while queue !=[]:
            tmp=queue[0]
            del queue[0]
            cnt+=1
            if tmp.left:
                queue.append(tmp.left)
                res.append(str(tmp.left.val))
            else:
                res.append("null")
            if tmp.right:
                queue.append(tmp.right)
                res.append(str(tmp.right.val))
            else:
                res.append("null")
            if cnt==last:
                cnt=0
                level+=1
                last =len(queue)
        return "["+",".join(res[0:2**level-1])+"]"


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        data=[None if str=="null" else int(str) for str in data.replace("[","").replace("]","").split(",")]
        queue=[]
        if data[0]:
            root=TreeNode(data[0])
            queue.append(root)
            index=1
            while index<len(data) and len(queue)>0:
                tmp = queue[0]
                del queue[0]
                if data[index]:
                    left =TreeNode(data[index])
                    tmp.left =left
                    queue.append(left)
                index+=1
                if index<len(data):
                    if data[index]:
                        right =TreeNode(data[index])
                        tmp.right =right
                        queue.append(right)
                index+=1
            return root


demo =Codec()
from BuildTree import binaryTree
arr=[10,9,11,8,None,None,12,7,None,None,13,6,None,None,14,5,None,None,15,4,None,None,16,3,None,None,17,2,None,None,18,1,None,None,19,0]
tree =binaryTree()
root =tree.build(arr)
data=demo.serialize(root)
print(data)
t=demo.deserialize(data)
print(demo.serialize(t))


