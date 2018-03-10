# -*- coding: utf-8 -*-
# @Time    : 18-3-10 下午7:03
# @Author  : Yeh
# @Email   : 576182627@qq.com
# @File    : Prime.py
# @Software: PyCharm

#求小于等于n的素数的个数
class Prime:
    def calc(self,n):
        prime=[]
        cnt=0
        vis=[False]*(n+1)
        for i in range(2,n):
            if vis[i]==False:
                prime.append(i)
                cnt+=1
            for j in range(0,cnt):
                if i*prime[j]<=n:
                    vis[i*prime[j]]=True
                    if i%prime[j]==0:break
                else:
                    break;
        return prime

demo =Prime()
param =demo.calc(1000)
print(param)
