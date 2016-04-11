#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-11 15:37:33
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        while node.next.next != None:
            node.val = node.next.val
        node.val = node.next.val
        node.next = None