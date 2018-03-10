# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 21:22
# @Author  : Yeh

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i]==-1:return False
            if visit[i]==1:return True
            visit[i]=-1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i]=1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


demo =Solution()
prerequisites = [[1,0]]
print(demo.canFinish(2, prerequisites))