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
        result = []
        return sum(self.helper(root, result))

    def helper(self, node, result=[]):
        tilt = 0
        if not node:
            result.append(0)
            return result
        if node.left:
            self.helper(node.left, result)
        if node.right:
            self.helper(node.right, result)
        sum_left = self.node_sum(node.left)
        sum_right = self.node_sum(node.right)
        tilt = abs(sum_left - sum_right)
        result.append(tilt)
        return result

    def node_sum(self, node):
        if not node:
            return 0
        if node.left is None and node.right is None:
            return node.val
        if node.left is None and node.right:
            return node.val + self.node_sum(node.right)
        if node.left and node.right is None:
            return node.val + self.node_sum(node.left)
        return node.val + self.node_sum(node.left) + self.node_sum(node.right)


if __name__ == '__main__':
    print Solution().findTilt(None)
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    # a.left.left = TreeNode(4)
    print Solution().node_sum(a)
    print Solution().findTilt(a)
    b = TreeNode(1)
    b.left = TreeNode(2)
    print Solution().findTilt(b)
    c = TreeNode(1)
    c.left = TreeNode(2)
    c.left.left = TreeNode(4)
    c.right = TreeNode(3)
    c.right.left = TreeNode(5)
    print Solution().findTilt(c)
