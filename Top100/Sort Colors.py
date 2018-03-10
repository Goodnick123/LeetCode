# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 10:23
# @Author  : Yeh
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        index=0
        while i<=j:
            if nums[i]==0:
                nums[index],nums[i]=nums[i],nums[index]
                index+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1


demo = Solution()
arr=[0]
print(demo.sortColors(arr))