# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 18:30
# @Author  : Yeh
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(sorted(nums),0,[],res)
        return res;
    def dfs(self,nums,index,lst,res):
        res.append(lst.copy())
        if index >=len(nums):
            return;
        for i in range(index,len(nums)):
            lst.append(nums[i])
            self.dfs(nums,i+1,lst,res)
            del lst[-1]




demo =Solution()
arr=[1,2,3]

print(demo.subsets(arr))