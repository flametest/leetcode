#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 17:35:14
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = None
        root = self.helper(preorder, inorder)
        return root

    def helper(self, preorder, inorder):
        node = None
        if preorder and inorder:
            node = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            preorder_left = preorder[1:i + 1]
            inorder_left = inorder[:i]
            node.left = self.helper(preorder_left, inorder_left)
            preorder_right = preorder[i + 1:]
            inorder_right = inorder[i + 1:]
            node.right = self.helper(preorder_right, inorder_right)
        return node


if __name__ == '__main__':
    print Solution().buildTree([10, 5, 4, 6, 15, 14, 16],
                               [4, 5, 6, 10, 14, 15, 16])
