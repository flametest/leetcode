#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-28 19:06:19
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if not root:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
            sum += root.left.val
        if root.left:
            sum += self.sumOfLeftLeaves(root.left)
        if root.right:
            sum += self.sumOfLeftLeaves(root.right)
        return sum


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print Solution().sumOfLeftLeaves(root)
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.right = TreeNode(3)
    root1.right.right.left = TreeNode(4)
    root1.right.right.right = TreeNode(5)
    print Solution().sumOfLeftLeaves(root1)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    print Solution().sumOfLeftLeaves(root2)

