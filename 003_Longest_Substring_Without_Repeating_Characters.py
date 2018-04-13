#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:46:17 2018

@author: yanghehuo
"""
# use harsh table to save used character. key is the character, value is the last index in the string of that character
# the first pointer scan over the entire array. the second pointer point to the end of substring without repeating character
# the second pointer only move forward

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {} # key is the character, value is the last index in the string of that character
        tail = 0
        max_len = 0
        for i,x in enumerate(s):
            if x in dic and tail <= dic[x]: # encounter character x, save the index
                tail = dic[x] + 1   
            else:
                max_len = max(max_len, i - tail + 1)
            dic[x] = i
        return max_len

s = Solution()
s.lengthOfLongestSubstring("abcabcbb")
s.lengthOfLongestSubstring("bbbbb")
s.lengthOfLongestSubstring("pwwkew")
s.lengthOfLongestSubstring("dvdf")
s.lengthOfLongestSubstring("tmmzuxt")
