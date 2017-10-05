#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-05 09:48:03
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t = l = None
        carry = 0
        while l1 or l2:
            ans = 0
            if l1:
                ans += l1.val
                l1 = l1.next
            if l2:
                ans += l2.val
                l2 = l2.next
            if carry:
                ans += carry
                carry = 0
            value = ans % 10
            carry = ans / 10
            if not l:
                l = ListNode(value)
                t = l
            else:
                l.next = ListNode(value)
                l = l.next
        if carry:
            l.next = ListNode(carry)
        return t




if __name__ == '__main__':
    a = ListNode(5)
    a.next = ListNode(4)
    a.next.next = ListNode(6)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    s = Solution()
    c = s.addTwoNumbers(a, b)
    while c:
        print c.val
        c = c.next
