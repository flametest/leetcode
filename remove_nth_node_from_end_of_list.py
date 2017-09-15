#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-15 17:44:39
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        r_head = p1 = p2 = head
        for _ in range(n):
            p1 = p1.next
        if not p1:
            return p2.next
        parent = p2
        while p1:
            p1 = p1.next
            parent = p2
            p2 = p2.next   
        parent.next = p2.next
        return r_head



if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    b = Solution().removeNthFromEnd(a, 2)
    while b:
        print b.val
        b = b.next
    c = Solution().removeNthFromEnd(ListNode(1), 1)
    while c:
        print c.val
        c = c.next
