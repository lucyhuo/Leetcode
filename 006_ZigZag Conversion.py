#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:48:44 2018

@author: yanghehuo
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        A = [''] * numRows
        direct = 1
        row_num = 0
        
        for x in s:
            A[row_num] += x # string + string = stringstring, concatenate
            
            if row_num == 0:
                direct = 1
            elif row_num == numRows -1:
                direct = -1
            
            row_num += direct
            
        return ''.join(A) # string has join method. join string element of sequence
                
s = Solution()
s.convert("ABCDEFGH",2)    
s.convert("GEEKSFORGEEKS",3)    

