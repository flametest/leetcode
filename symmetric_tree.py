#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-18 16:23:25
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = root.left
        right = root.right
        return self.is_same_tree(self.invert_tree(left), right)

    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def invert_tree(self, root):
        if not root:
            return root
        if root.left:
            self.invert_tree(root.left)
        if root.right:
            self.invert_tree(root.right)
        root.left, root.right = root.right, root.left
        return root
        


if __name__ == '__main__':
    # a = TreeNode(1)
    # a.left = TreeNode(2)
    # a.right = TreeNode(2)
    # a.left.left = TreeNode(3)
    # a.left.right = TreeNode(4)
    # a.right.left = TreeNode(4)
    # a.right.right = TreeNode(3)
    # print Solution().isSymmetric(a)
    # b = TreeNode(1)
    # b.left = TreeNode(2)
    # b.right = TreeNode(2)
    # b.left.right = TreeNode(3)
    # b.right.right = TreeNode(3)
    # print Solution().isSymmetric(b)
    c = TreeNode(1)
    c.left = TreeNode(2)
    print Solution().isSymmetric(c)
