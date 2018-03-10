# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 23:07
# @Author  : Yeh

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None: return None;
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>1:
                return i

    def bitmap(self,nums):
        if nums is None: return None
        n=0
        for i in nums:
            cnt=((n&(0x1<<i))>>i)
            cnt+=1
            if cnt==2:
                return i
            else:
                n&=~(0x1<<i)
                n|=(cnt<<i)
    def binarySearch(self,nums):
        if nums is None: return None
        first,last=len(nums)-1
        while first<=last:
            mid =(first+last)//2
            cnt=0
            for i in nums:
                if(i<=nums[mid]):
                    cnt+=1
            if cnt>mid:
                last =mid-1
            else:
                first=mid+1
        return nums[first]



demo =Solution()
arr=[1,1]
param=demo.bitmap(arr)
print(param)