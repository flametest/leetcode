#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-03 15:01:13
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    #     if not root or not p or not q:
    #         return
    #     root_to_p = list(self.get_root_path(root, p))
    #     root_to_q = list(self.get_root_path(root, q))
    #     for x in root_to_p[0]:
    #         for y in root_to_q[0]:
    #             if x is y:
    #                 return x

    # def get_root_path(self, root, node):
    #     if root is node:
    #         yield [root]
    #     if root.left:
    #         for i in self.get_root_path(root.left, node):
    #             yield i + [root]
    #     if root.right:
    #         for j in self.get_root_path(root.right, node):
    #             yield j + [root]

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root in [None, p, q]:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


if __name__ == '__main__':
    a = TreeNode(3)
    a.left = TreeNode(5)
    a.right = TreeNode(1)
    a.left.left = TreeNode(6)
    a.left.right = TreeNode(2)
    a.left.right.left = TreeNode(7)
    a.left.right.right = TreeNode(4)
    s = Solution()
    # gen = s.get_root_path(a, a.left.left)
    print s.lowestCommonAncestor(a, a.left, a.right).val
    print s.lowestCommonAncestor(a, a.left, a.left.right.right).val
    print s.lowestCommonAncestor(None, None, None)
