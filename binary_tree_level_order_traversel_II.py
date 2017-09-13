#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-29 09:41:44
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        result = []
        if not root:
            return result
        import Queue
        q = Queue.Queue()
        q.put(root)
        while True:
            row = []
            while not q.empty():
                e = q.get()
                row.append(e)
            for j in row:
                if j.left:
                    q.put(j.left)
                if j.right:
                    q.put(j.right)
            result.append([i.val for i in row])
            if q.empty():
                break
        return result


if __name__ == '__main__':
    a = TreeNode(3)
    a.left = TreeNode(9)
    a.right = TreeNode(20)
    a.right.left = TreeNode(15)
    a.right.right = TreeNode(7)
    print Solution().levelOrderBottom(a)
    print Solution().levelOrderBottom(None)
    b = TreeNode(5)
    print Solution().levelOrderBottom(b)
    c = TreeNode(1)
    c.left = TreeNode(2)
    c.right = TreeNode(3)
    c.left.left = TreeNode(4)
    c.right.right = TreeNode(5)
    print Solution().levelOrderBottom(c)
