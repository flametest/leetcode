#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-16 18:39:34
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        stack1 = [root]
        stack2 = []
        while True:
            tmp1 = []
            while stack1:
                node1 = stack1.pop()
                tmp1.append(node1.val)
                if node1.left:
                    stack2.append(node1.left)
                if node1.right:
                    stack2.append(node1.right)
            if tmp1:
                result.append(tmp1)
            tmp2 = []
            while stack2:
                node2 = stack2.pop()
                tmp2.append(node2.val)
                if node2.right:
                    stack1.append(node2.right)
                if node2.left:
                    stack1.append(node2.left)
            if tmp2:
                result.append(tmp2)
            if not stack1 and not stack2:
                break
        return result


if __name__ == '__main__':
    a = TreeNode(3)
    a.left = TreeNode(9)
    a.right = TreeNode(20)
    a.right.left = TreeNode(15)
    a.right.right = TreeNode(7)
    s = Solution()
    print s.zigzagLevelOrder(a)
    print s.zigzagLevelOrder(None)
