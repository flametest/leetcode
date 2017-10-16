#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-16 16:40:16
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        copy_nums = [i for i in self.nums]
        for i, num in enumerate(copy_nums):
            rint = random.randint(0, i)
            copy_nums[i],  copy_nums[rint] = copy_nums[rint],  copy_nums[i]
        return copy_nums
                
        


# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
obj = Solution(nums)
# param_0 = obj.shuffle()
param_1 = obj.reset()
# print param_1
param_2 = obj.shuffle()
print param_2
