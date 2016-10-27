#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-27 14:28:20
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = r = 1
        if not root:
            return 0
        if root.left != None:
            l += self.maxDepth(root.left)
        if root.right != None:
            r += self.maxDepth(root.right)

        return max(l, r)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print Solution().maxDepth(root)