#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-18 08:33:30
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
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)

    def helper(self, root, min_val=float("inf")):
        if not root:
            return min_val
        if root.left:
            right_most = self.find_right_most(root.left)
            if root.val - right_most.val < min_val:
                min_val = root.val - right_most.val
        if root.right:
            left_most = self.find_left_most(root.right)
            if left_most.val - root.val < min_val:
                min_val = left_most.val - root.val
        min_val = min(self.helper(root.left, min_val),
                      self.helper(root.right, min_val))
        return min_val

    def find_left_most(self, root):
        if not root.left:
            return root
        return self.find_left_most(root.left)

    def find_right_most(self, root):
        if not root.right:
            return root
        return self.find_right_most(root.right)


if __name__ == '__main__':
    a = TreeNode(1)
    a.right = TreeNode(3)
    a.right.left = TreeNode(2)
    print Solution().helper(a)
    print Solution().getMinimumDifference(a)
    b = TreeNode(236)
    b.left = TreeNode(104)
    b.right = TreeNode(701)
    b.left.right = TreeNode(227)
    b.right.right = TreeNode(911)
    print Solution().getMinimumDifference(b)
