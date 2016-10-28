#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-28 15:31:36
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        if p.left and q.left:
            if not self.isSameTree(p.left, q.left):
                return False
        if p.right and q.right:
            if not self.isSameTree(p.right, q.right):
                return False
        if p.left is None and q.left is not None:
            return False
        if p.left is not None and q.left is None:
            return False
        if p.right is None and q.right is not None:
            return False
        if p.right is not None and q.right is None:
            return False
        return True


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.left.left = TreeNode(4)
    print Solution().isSameTree(p, q)