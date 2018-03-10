# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 21:56
# @Author  : Yeh


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow =head
        fast =head
        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
            if slow ==fast:
                break
        if fast == None and fast.next ==None :
            return None
        index =head
        while index!=slow:
            index =index.next
            slow =slow.next
        return index

demo =Solution()
head =[]
demo.detectCycle(head)