# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 16:51
# @Author  : Yeh
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h=ListNode(-1)
        while head:
            tmp =head
            head =head.next
            tmp.next =h.next
            h.next =tmp
        return h.next



demo =Solution()
head =ListNode(1)
node1 =ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
head.next =node1
node1.next =node2
node2.next = node3
r=demo.reverseList(head)
while r:
    print(r.val)
    r =r.next
