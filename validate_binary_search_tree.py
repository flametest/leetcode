#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-22 01:24:08
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if (root.left and not self.is_valid(root, root.left, ">"))\
                or (root.right and not self.is_valid(root, root.right, "<")):
            return False
        return self.isValidBST(root.right) and self.isValidBST(root.left)

    def is_valid(self, root1, root2, sign):
        result = []
        subtree_vals = self.get_subtree_vals(root2, result)
        if sign == ">":
            return all([root1.val > i for i in subtree_vals])
        if sign == "<":
            return all([root1.val < i for i in subtree_vals])

    def get_subtree_vals(self, root, result=[]):
        if root:
            result.append(root.val)
        if root.left:
            self.get_subtree_vals(root.left, result)
        if root.right:
            self.get_subtree_vals(root.right, result)
        return result


if __name__ == '__main__':
    a = TreeNode(2)
    a.left = TreeNode(1)
    a.right = TreeNode(3)
    print Solution().isValidBST(a)  # True
    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)
    print Solution().isValidBST(b)  # False
    c = TreeNode(1)
    c.left = TreeNode(1)
    print Solution().isValidBST(c)  # False
    d = TreeNode(10)
    d.left = TreeNode(5)
    d.right = TreeNode(15)
    d.right.left = TreeNode(6)
    d.right.right = TreeNode(20)
    print Solution().isValidBST(d)
    # print Solution().get_subtree_vals(d)
    # print Solution().is_valid(d, d.left, ">=")
