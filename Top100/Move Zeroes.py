# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 23:19
# @Author  : Yeh

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur=0
        for i in range(len(nums)):
            if nums[i]!=0 :
                if i==cur:
                    cur+=1
                else:
                    nums[cur]=nums[i]
                    nums[i]=0
                    cur+=1
        #print(nums)
demo =Solution()
nums=[]
demo.moveZeroes(nums)

