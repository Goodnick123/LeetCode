# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 15:21
# @Author  : Yeh

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map ={}
        for ch in t:
            map[ch]=map.get(ch,0)+1
        left=0;cnt=0;minNum=len(s)+1;bakeLeft=0
        for i in range(len(s)):
             if map.get(s[i])is not None:
                 map[s[i]] = map.get(s[i]) -1
                 if map[s[i]]>=0:
                     cnt+=1
                 while cnt ==len(t):
                     if i-left+1<minNum:
                         minNum =min(i-left+1,minNum)
                         bakeLeft =left
                     if map.get(s[left]) is not None:
                         map[s[left]] = map[s[left]] + 1
                         if map[s[left]]>0:
                             cnt-=1
                     left+=1
        return "" if minNum>len(s) else "".join(s[bakeLeft:minNum+bakeLeft])

demo = Solution()
print(demo.minWindow("cabwefgewcwaefgcf","cae"))










demo =Solution()
demo.minWindow("ADCBCO", "AABC")