#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-20 16:32:26
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
    # def pathSum(self, root, sum):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: int
    #     """
    #     result = 0
    #     if not root:
    #         return 0
    #     if root.left:
    #         result += self.pathSum(root.left, sum)
    #     if root.right:
    #         result += self.pathSum(root.right, sum)
    #     for i in self.helper(root, 0, sum):
    #         result += 1
    #     return result

    # def helper(self, node, tmp, sum):
    #     if node.val + tmp == sum:
    #         yield [node.val]
    #     if node.left:
    #         for i in self.helper(node.left, node.val + tmp, sum):
    #             yield [node.val] + i
    #     if node.right:
    #         for j in self.helper(node.right, node.val + tmp, sum):
    #             yield [node.val] + j
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.helper(root, sum, [sum])

    def helper(self, node, sum, mid_list):
        res = 0
        if not node:
            return res
        for mid_val in mid_list:
            if mid_val == node.val:
                res += 1
        mid_list = [i - node.val for i in mid_list]
        mid_list.append(sum)
        if node.left:
            res += self.helper(node.left, sum - node.val, mid_list)
        if node.right:
            res += self.helper(node.right, sum - node.val, mid_list)
        return res

if __name__ == '__main__':
    a = TreeNode(10)
    a.left = TreeNode(5)
    a.right = TreeNode(-3)
    a.left.left = TreeNode(3)
    a.left.right = TreeNode(2)
    a.left.left.left = TreeNode(3)
    a.left.left.right = TreeNode(-2)
    a.left.right.right = TreeNode(1)
    a.right.right = TreeNode(11)
    print Solution().pathSum(a, 8)
