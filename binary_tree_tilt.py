#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 17:18:54
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
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return abs(self.node_sum(root.left) - self.node_sum(root.right))

    def node_sum(self, node):
        if node.left is None and node.right is None:
            return node.val
        if node.left is None and node.right:
            return node.val + self.node_sum(node.right)
        if node.left and node.right is None:
            return node.val + self.node_sum(node.left)
        return node.val + self.node_sum(node.left) + self.node_sum(node.right)


if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    # a.left.left = TreeNode(4)
    print Solution().node_sum(a)
    print Solution().findTilt(a)
