#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 02:49:03
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        if not head:
            return True
        while head:
            vals.append(head.val)
            head = head.next
        vals1 = vals[::-1]
        for i in range(len(vals)):
            if vals[i] != vals1[i]:
                return False
        return True


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(1)
    print Solution().isPalindrome(a)
