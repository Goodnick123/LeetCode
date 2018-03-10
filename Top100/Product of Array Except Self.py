# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 20:45
# @Author  : Yeh
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None:return 0
        left=[0]*len(nums)
        right=[0]*len(nums)
        left[0],right[len(nums)-1]=1,1
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
            right[len(nums)-1-i]=right[len(nums)-i]*nums[len(nums)-i]
        return [left[i]*right[i] for i in range(len(nums))]

demo =Solution()
arr=[1,0,2]
print(demo.productExceptSelf(arr))