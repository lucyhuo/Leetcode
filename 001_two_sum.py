
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:46:17 2018

@author: yanghehuo
"""
# use hashmap
# track the Right operand in order for the sum to meet the target.
# Save the left operand's index as value where the key is the right operand"

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n],i]
            else:
                dic[target - n] = i
   