#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-29 09:41:44
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        import Queue
        q = Queue.Queue()
        q.put(root)
        q.put("r")
        row = []
        while q.qsize():
            e = q.get()
            if e == "r":
                if row:
                    result.append(row)
                row = []
                continue
            row.append(e.val)
            if e.left:
                q.put(e.left)
            if e.right:
                q.put(e.right)
            q.put("r")
        return result[::-1]


if __name__ == '__main__':
    a = TreeNode(3)
    a.left = TreeNode(9)
    a.right = TreeNode(20)
    a.right.left = TreeNode(15)
    a.right.right = TreeNode(7)
    print Solution().levelOrderBottom(a)
