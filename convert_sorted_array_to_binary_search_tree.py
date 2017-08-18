#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-18 21:19:07
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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.slash(nums)

    def slash(self, nums):
        if not nums:
            return None
        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.slash(nums[:mid])
        root.right = self.slash(nums[(mid + 1):])
        return root

    def insert_node(self, x, T):
        if T is None:
            return TreeNode(x)
        elif x < T.val:
            T.left = self.insert_node(x, T.left)
        elif x > T.val:
            T.right = self.insert_node(x, T.right)
        return T

    def traversal(self, T):
        if not T:
            return
        self.traversal(T.left)
        print T.val
        self.traversal(T.right)


if __name__ == '__main__':
    x = Solution().sortedArrayToBST([0, 1, 2, 3, 4, 5])
    Solution().traversal(x)
