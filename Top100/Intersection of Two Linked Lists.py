# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 20:36
# @Author  : Yeh

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stackA =[]
        stackB =[]
        while headA :
            stackA.append(headA)
            headA =headA.next
        while headB:
            stackB.append(headB)
            headB =headB.next
        tmp =None
        if stackA and stackB:
            while stackA and stackB and stackA[-1] == stackB[-1]:
                tmp =stackA[-1]
                del stackA[-1]
                del stackB[-1]
            return tmp
        else:
            return None



demo =Solution()
headA = ListNode(1)
node1 =ListNode(3)
node2 =ListNode(4)
node1.next =node2
headA.next =node1
headB = ListNode(2)
node3 =ListNode(5)
headB.next =node3
commNode1 =ListNode(9)
commNode2 =ListNode(8)
commNode1.next=commNode2
node2.next =commNode1
node3.next =commNode1
print(demo.getIntersectionNode(headA,headB).val)




