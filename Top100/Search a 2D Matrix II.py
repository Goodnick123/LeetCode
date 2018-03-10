# -*- coding: utf-8 -*-
# @Time    : 18-3-5 下午4:08
# @Author  : Yeh
# @File    : Search a 2D Matrix II.py
# @Software: PyCharm

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:return False
        rows=len(matrix)
        cols=len(matrix[0])
        if target < matrix[0][0] or target > matrix[rows - 1][cols - 1]:
            return False
        for  i in range(rows):
           if target>=matrix[i][0] and target<=matrix[i][cols-1]:
               first,last =0,cols-1
               while first<=last:
                   mid = (first+last)//2
                   if matrix[i][mid] == target:return True
                   elif matrix[i][mid]<target :
                       first = mid +1
                   else:
                       last = mid-1

        return False

demo =Solution()
matrix =[[-1],[-1]]
param = demo.searchMatrix(matrix,-1)
print(param)


