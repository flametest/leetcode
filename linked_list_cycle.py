#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-24 00:18:25
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while True:
            # fast pointer is faster, so we just
            # check the fast and its next pointer
            if not fast or not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = a
    print Solution().hasCycle(a)
    print Solution().hasCycle([])
    print Solution().hasCycle(ListNode(1))
