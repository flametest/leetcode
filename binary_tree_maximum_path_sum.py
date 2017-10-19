#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-16 19:10:04
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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.sum_val = -float("inf")

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.sum_val = max(self.sum_val, left + right + root.val)
            return max((max(left, right) + root.val), 0)
        dfs(root)
        return self.sum_val


if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)
    s = Solution()
    print s.maxPathSum(a) # 11
    b = TreeNode(-3)
    print s.maxPathSum(b) # -3
    c = TreeNode(2)
    c.left = TreeNode(-1)
    print s.maxPathSum(c) # 2
    d = TreeNode(-2)
    d.left = TreeNode(1)
    print s.maxPathSum(d) # 1
    e = TreeNode(1)
    e.left = TreeNode(-2)
    e.right = TreeNode(3)
    print s.maxPathSum(e) # 4
