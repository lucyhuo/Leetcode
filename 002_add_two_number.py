#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:40:17 2018

@author: yanghehuo
"""

# Definition for singly-linked list.

# while l1 is not null or l2 is not null or carry is not 0, loop continues
# if l1 (or l2) is null, simply consider it as zero.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, value = divmod(carry,10)
            n.next = ListNode(value)
            n = n.next
        return dummy.next