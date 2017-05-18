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
        min_val = float("inf")
        result = self.traverse_tree(root)
        for k, i in enumerate(result):
            for j in result[k + 1:]:
                if abs(i - j) < min_val:
                    min_val = abs(i - j)
        return min_val

    def traverse_tree(self, node):
        result = []
        if node.left:
            result.extend(self.traverse_tree(node.left))
        result.append(node.val)
        if node.right:
            result.extend(self.traverse_tree(node.right))
        return result


if __name__ == '__main__':
    a = TreeNode(1)
    a.right = TreeNode(3)
    a.right.left = TreeNode(2)
    print Solution().traverse_tree(a)
    print Solution().getMinimumDifference(a)
