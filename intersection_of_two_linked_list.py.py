#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-03 09:26:37
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


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
        a = headA
        len_a = 0
        while a:
            len_a += 1
            a = a.next
        b = headB
        len_b = 0
        while b:
            len_b += 1
            b = b.next
        a1 = headA
        b1 = headB
        if len_a > len_b:
            pre = len_a - len_b
            while pre:
                a1 = a1.next
                pre -= 1
        else:
            pre = len_b - len_a
            while pre:
                b1 = b1.next
                pre -= 1
        while a1 and b1:
            if a1 is b1:
                return a1
            a1 = a1.next
            b1 = b1.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    b = ListNode(6)
    b.next = ListNode(7)
    b.next.next = ListNode(8)
    b.next.next.next = ListNode(9)
    b.next.next.next.next = a.next.next
    c = Solution()
    print c.getIntersectionNode(a, b).val
    print c.getIntersectionNode(None, b)
    print c.getIntersectionNode(a, None)
    print c.getIntersectionNode(None, None)
