#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-22 16:11:21
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if root:
            stack.append(root)
        else:
            return []
        visited = []
        while True:
            if stack:
                tmp = stack[-1]
            if tmp and tmp.left and (tmp.left not in visited):
                stack.append(tmp.left)
                tmp = tmp.left
                continue
            if stack:
                node = stack.pop()
                visited.append(node)
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
            else:
                break
        return result


if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.left.right = TreeNode(3)
    print Solution().inorderTraversal(a)
    b = TreeNode(10)
    b.left = TreeNode(5)
    b.right = TreeNode(15)
    b.left.right = TreeNode(6)
    b.right.right = TreeNode(20)
    print Solution().inorderTraversal(b)
