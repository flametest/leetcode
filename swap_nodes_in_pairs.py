#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-28 22:14:49
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            n = head.next
            head.next = self.swapPairs(n.next)
            n.next = head
            return n
        return head


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    b = Solution().swapPairs(a)
    while b:
        print b.val
        b = b.next
