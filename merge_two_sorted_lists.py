#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-05 11:53:41
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        head = l = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        l.next = self.mergeTwoLists(l1, l2)
        return head.next

            


if __name__ == '__main__':
    # a = ListNode(1)
    # a.next = ListNode(2)
    # a.next.next = ListNode(3)
    # b = ListNode(4)
    # b.next = ListNode(5)
    # b.next.next = ListNode(6)
    # s = Solution()
    # print s.mergeTwoLists(a, b)
    c = ListNode(1)
    c.next = ListNode(3)
    c.next.next = ListNode(5)
    d = ListNode(2)
    d.next = ListNode(4)
    d.next.next = ListNode(6)
    s = Solution()
    print s.mergeTwoLists(c, d)

