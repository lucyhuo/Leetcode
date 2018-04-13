#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:00:32 2018

@author: yanghehuo
"""

# remember edge condition, eg length < 3
# using only the first of all same values to remove duplicates in result



class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # edge condition
        
        length = len(nums)
        
        if length < 3:
            return []
        elif length == 3:
            if sum(nums) ==0:
                return [nums]
            else:
                return []
        
        nums.sort()
        res = []
        
        
        for i in range(length-2):
        # only use the first of all same values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r < length-1 and nums[r] == nums[r-1]:
                    r -= 1
                    continue
                s = nums[i] + nums[l] + nums[r]
                if (s) == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

                elif (s) < 0:
                    l += 1
                else:
                    r -= 1
        return res


            
s = Solution()

s.threeSum([-1,0,1])
s.threeSum([-1,0,1,2,-1,-4])

s.threeSum([0,0,0,0])

