#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 23:52:40
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = float("inf")   
    
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.min_val:
            self.min_val = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        pop_val = self.stack.pop()
        if pop_val == self.min_val:
            self.min_val = float("inf")
            self.min_val = self.getMin()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack and self.min_val == float("inf"):
            for i in self.stack:
                if i < self.min_val:
                    self.min_val = i
        return self.min_val


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print obj.getMin()
    print obj.pop()
    print obj.top()
    print obj.getMin()
