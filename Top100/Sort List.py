# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 20:57
# @Author  : Yeh

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head ==None :
            return head
        if head.next ==None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow =slow.next
            fast = fast.next.next
        mid =slow
        midNext = mid.next
        mid.next = None
        left =self.sortList(head)
        right=self.sortList(midNext)
        return self.merge(left,right)

    def merge(self,left,right):
        if left==None:
            return right
        if right ==None:
            return left
        head =None
        if left.val<right.val:
            head =left
            left =left.next
        else:
            head =right
            right = right.next
        curIndex = head
        while left and right:
            if left.val<right.val:
                curIndex.next =left
                left  =left.next
                curIndex =curIndex.next
            else:
                curIndex.next =right
                right =right.next
                curIndex =curIndex.next
        if left:curIndex.next=left
        if right:curIndex.next=right
        return head

demo =Solution()
node1 =ListNode(1)
node2 =ListNode(3)
node3 =ListNode(4)
node4 =ListNode(2)
node1.next =node2
node2.next= node3
node3.next= node4
head =demo.sortList(node1)
while head:
    print(head.val)
    head =head.next



