#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-22 14:58:07
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
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
        if head is None or head.next is None:
            return head
        slow = fast = head
        mid = None
        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        head = l = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next
        while l1:
            l.next = ListNode(l1.val)
            l1 = l1.next
            l = l.next
        while l2:
            l.next = ListNode(l2.val)
            l2 = l2.next
            l = l.next
        return head.next


if __name__ == '__main__':
    a = ListNode(5)
    a.next = ListNode(6)
    a.next.next = ListNode(4)
    a.next.next.next = ListNode(7)
    s = Solution()
    b = s.sortList(a)
    while b:
        print b.val
        b = b.next

    c = ListNode(3)
    c.next = ListNode(2)
    c.next.next = ListNode(4)
    d = s.sortList(c)
    while d:
        print d.val
        d = d.next
