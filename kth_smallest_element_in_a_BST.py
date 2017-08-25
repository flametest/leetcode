#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-25 21:40:27
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
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        vals = []
        vals = self.find_all_element(root, vals)
        return vals[k-1]

    def find_all_element(self, root, result=[]):
        if not root:
            return
        self.find_all_element(root.left, result)
        result.append(root.val)
        self.find_all_element(root.right, result)
        return result


if __name__ == '__main__':
    a = TreeNode(10)
    a.left = TreeNode(5)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(6)
    a.right = TreeNode(15)
    a.right.left = TreeNode(14)
    a.right.right = TreeNode(16)
    print Solution().kthSmallest(a, 6)
    print Solution().find_all_element(a)
    b = TreeNode(2)
    b.left = TreeNode(1)
    print Solution().kthSmallest(b, 2)

