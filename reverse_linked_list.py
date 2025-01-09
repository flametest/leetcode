#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-03 16:14:25
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/reverse-linked-list/
# @Version : $Id$
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x = None
        count = 0
        while head:
            t = ListNode(head.val)
            if count == 0:
                t.next = None
            else:
                t.next = x
            x = t
            head = head.next
            count += 1
        return x


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# watch this video: https://www.youtube.com/watch?v=G0_I-ZF0S38
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    x = Solution().reverseList(head)
    while x:
        print(x.val)
        x = x.next

    y = Solution1().reverseList(head)
    while y:
        print(y.val)
        y = y.next
