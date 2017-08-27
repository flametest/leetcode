#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-27 16:06:25
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # old_map = {}
        # new_head = RandomListNode(head.label)
        # old_map[id(head)] = new_head
        # if head.random:
        #     new_head.random = RandomListNode(head.random.label)
        #     old_map[id(head.random)] = new_head.random
        # r_head = new_head
        # while head.next:
        #     head = head.next
        #     if id(head) not in old_map:
        #         new_head.next = RandomListNode(head.label)
        #         old_map[id(head)] = new_head.next
        #         if head.random and id(head.random) not in old_map:
        #             new_head.next.random = RandomListNode(head.random.label)
        #             old_map[id(head.random)] = new_head.random
        #         elif head.random and id(head.random) in old_map:
        #             new_head.next.random = old_map[id(head.random)]
        #     else:
        #         new_head.next = old_map[id(head)]
        #     new_head = new_head.next
        # if head.random:
        #     new_head.random = old_map[id(head.random)]
        # return r_head
        if not head:
            return head
        node_mapping = {}
        new_head = RandomListNode(head.label)
        node_mapping[hex(id(head))] = new_head
        if head.random:
            new_head.random = head.random
        a_head = new_head
        while head.next:
            head = head.next
            new_head.next = RandomListNode(head.label)
            if head.random:
                new_head.next.random = head.random
            node_mapping[hex(id(head))] = new_head.next
            new_head = new_head.next
        if head.random:
            new_head.random = head.random
        r_head = a_head
        while a_head:
            if a_head.random and hex(id(a_head.random)) in node_mapping:
                a_head.random = node_mapping[hex(id(a_head.random))]
            a_head = a_head.next
        return r_head


if __name__ == '__main__':
    a = RandomListNode(1)
    a.next = RandomListNode(2)
    a.next.next = RandomListNode(3)
    a.random = a.next.next
    a.next.random = a
    a.next.next.random = a.next
    b = Solution().copyRandomList(a)

    # c = RandomListNode(-1)
    # c.next = RandomListNode(-1)
    # c.random = c.next
    # c.next.random = c
    # d = Solution().copyRandomList(c)
