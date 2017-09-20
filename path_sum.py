#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-20 15:47:40
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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root and sum != 0:
            return False
        elif not root and sum == 0:
            return True
        return self.helper(root, 0, sum)

    def helper(self, node, tmp, sum):
        if node.val + tmp == sum and not node.left and not node.right:
            return True
        if node.left and self.helper(node.left, node.val + tmp, sum):
            return True
        if node.right and self.helper(node.right, node.val + tmp, sum):
            return True
        return False


if __name__ == '__main__':
    a = TreeNode(5)
    a.left = TreeNode(4)
    a.right = TreeNode(8)
    a.left.left = TreeNode(11)
    a.left.left.left = TreeNode(7)
    a.left.left.right = TreeNode(2)
    a.right.left = TreeNode(13)
    a.right.right = TreeNode(4)
    a.right.right.right = TreeNode(1)
    print Solution().hasPathSum(a, 22)
    print Solution().hasPathSum(None, 1)
    b = TreeNode(1)
    b.right = TreeNode(2)
    print Solution().hasPathSum(b, 1)
        
