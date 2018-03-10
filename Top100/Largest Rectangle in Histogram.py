# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 15:24
# @Author  : Yeh
#TLE
class Solution:
    def largestRectangleArea1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        maxS=0
        for i in range(len(heights)):
            left =i-1
            right=i+1
            cnt = 1
            while left>=0 and heights[i]<=heights[left]:
                left-=1
                cnt+=1
            while right<len(heights) and heights[i]<=heights[right]:
                right+=1
                cnt+=1
            maxS=max(maxS,heights[i]*cnt)
        return maxS
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        maxS=0
        for i in range(len(heights)):
            if stack==[] or stack[-1] <= heights[i]:
                stack.append(heights[i])
            else:
                cnt=0
                index= len(stack)-1
                while stack !=[] and stack[-1]>heights[i]:
                    cnt+=1
                    maxS =max(maxS,cnt*stack[-1])
                    del stack[-1]
                while cnt>=0:
                    stack.append(heights[i])
                    cnt-=1
        cnt=1
        while stack!=[]:
            maxS =max(maxS,cnt*stack[-1])
            del stack[-1]
            cnt+=1
        return maxS

demo = Solution()
height = [2,1,5,6,2,3]
print(demo.largestRectangleArea(height))
