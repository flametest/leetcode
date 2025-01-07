#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-05 09:48:03
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        cur3 = l3

        while True:
            addup = 0
            if l1 is not None and l2 is not None:
                addup = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 is None and l2 is not None:
                addup = l2.val
                l2 = l2.next
            elif l1 is not None and l2 is None:
                addup = l1.val
                l1 = l1.next
            else:
                break

            total = cur3.val + addup
            value = total % 10
            carry = total // 10
            cur3.val = value
            if l1 or l2 or carry:
                cur3.next = ListNode(carry)
            cur3 = cur3.next
        return l3


if __name__ == '__main__':
    a = ListNode(5)
    a.next = ListNode(4)
    a.next.next = ListNode(6)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    s = Solution1()
    c = s.addTwoNumbers(a, b)
    while c:
        print(c.val)
        c = c.next
