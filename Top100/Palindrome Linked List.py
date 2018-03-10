# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 16:29
# @Author  : Yeh
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:return True
        slow=fast=head
        stack=[]
        while fast and fast.next:
            stack.insert(0,slow.val)
            fast =fast.next.next
            slow =slow.next
        print(stack)
        if fast :
            slow =slow.next
        for i in stack:
            if i!=slow.val:
                return False
            slow =slow.next
        return True


demo =Solution()
head =ListNode(3)
node1=ListNode(2)
node2=ListNode(1)
node3=ListNode(2)
node4=ListNode(3)
head.next =node1
# node1.next =node2
# node2.next =node3
# node3.next =node4
print(demo.isPalindrome(head))
