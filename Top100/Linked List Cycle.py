# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 18:03
# @Author  : Yeh
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow =slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False


