#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-05 10:46:18
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution(object):
#     def evalRPN(self, tokens):
#         """
#         :type tokens: List[str]
#         :rtype: int
#         """
#         stack = []
#         for token in tokens:
#             try:
#                 int(token)
#                 stack.append(TreeNode(token))
#             except ValueError:
#                 if token not in ["+", "-", "*", "/"]:
#                     continue
#                 tmp = []
#                 n = 0
#                 while stack and n < 2:
#                     n += 1
#                     tmp.append(stack.pop())
#                 new_node = TreeNode(token)
#                 if len(tmp) == 2:
#                     new_node.right = tmp[0]
#                     new_node.left = tmp[1]
#                 elif len(tmp) == 1:
#                     new_node.right = tmp[0]
#                 stack.append(new_node)
#         new_order = []
#         self.inorder_traverse(stack.pop(), new_order)
#         return eval("".join(new_order))

#     def inorder_traverse(self, root, result=[]):
#         if not root:
#             return
#         result.append("(")
#         self.inorder_traverse(root.left, result)
#         result.append(root.val)
#         self.inorder_traverse(root.right, result)
#         result.append(")")
#         return result


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            try:
                int(token)
                stack.append(token)
            except ValueError:
                if token not in ["+", "-", "*", "/"]:
                    continue
                n = 0
                tmp = []
                while stack and n < 2:
                    n += 1
                    tmp.append(stack.pop())
                if token == "/":
                    tmp_result = int(float(tmp[1]) / int(tmp[0]))
                else:
                    tmp_result = eval(tmp[1] + token + tmp[0])
                stack.append(str(tmp_result))
        return int(stack.pop())


if __name__ == '__main__':
    s = Solution()
    print s.evalRPN(["2", "1", "+", "3", "*"])
    print s.evalRPN(["4", "13", "5", "/", "+"])
    print s.evalRPN(["18"])
    print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
