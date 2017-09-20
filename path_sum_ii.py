#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-20 16:02:56
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        for i in self.helper(root, 0, sum):
            result.append(i)
        return result

    def helper(self, node, tmp, sum):
        if node.val + tmp == sum and not node.left and not node.right:
            yield [node.val]
        if node.left:
            left_val = self.helper(node.left, node.val + tmp, sum)
            for i in left_val:
                yield [node.val] + i
        if node.right:
            right_val = self.helper(node.right, node.val + tmp, sum)
            for j in right_val:
                yield [node.val] + j


if __name__ == '__main__':
    a = TreeNode(5)
    a.left = TreeNode(4)
    a.right = TreeNode(8)
    a.left.left = TreeNode(11)
    a.left.left.left = TreeNode(7)
    a.left.left.right = TreeNode(2)
    a.right.left = TreeNode(13)
    a.right.right = TreeNode(4)
    a.right.right.left = TreeNode(5)
    a.right.right.right = TreeNode(1)
    print Solution().pathSum(a, 22)
    b = TreeNode(1)
    print Solution().pathSum(b, 1)
        