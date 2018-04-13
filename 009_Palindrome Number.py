#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:19:33 2018

@author: yanghehuo
"""

# floor division is //
# no extra space
# find the leftmost digit of a int: x // keeper where keeper = 10 ^ int(log(x,10))
# find the rightmost digit of a int: x % 10

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        keeper = 1
        while x // keeper >= 10:
            keeper *= 10
        
        while x > 0:
            left = x // keeper
            right = x % 10
            
            if left != right:
                return False
            
            x = (x % keeper) //10
            keeper //= 100
            
        return True
    
s = Solution()
s.isPalindrome(1221)

