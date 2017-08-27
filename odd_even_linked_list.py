#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-27 00:19:52
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd_head = head
        even_head = head.next
        o_head = odd_head
        e_head = even_head

        while head and head.next is not None:
            head = head.next.next
            if head:
                odd_head.next = head
                even_head.next = head.next
                odd_head = odd_head.next
                even_head = even_head.next
        odd_head.next = e_head
        return o_head


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = ListNode(6)
    b = Solution().oddEvenList(a)
    while b:
        print b.val
        b = b.next
    c = ListNode(1)
    d = Solution().oddEvenList(c)
    while d:
        print d.val
        d = d.next
    print Solution().oddEvenList(None)
