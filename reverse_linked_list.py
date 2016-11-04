#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-03 16:14:25
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

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
                t.next  = None
            else:
                t.next = x
            x = t
            head = head.next
            count  += 1
        return x         
        

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print Solution().reverseList(head)
    while head:
        print head.val
        head = head.next

