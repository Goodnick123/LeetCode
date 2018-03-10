class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,0,len(nums),res)
        print(res)
        return res
    def dfs(self,nums,index,n,res):
        if(index==n-1):
            res.append(nums.copy())
        else:
            for i in range(index,n):
                self.swap(nums,index,i)
                self.dfs(nums,index+1,n,res)
                self.swap(nums,i,index)

    def swap(self,nums,i,j):
        tmp=nums[i]
        nums[i]=nums[j]
        nums[j] =tmp

s=Solution()
nums=[]
list=s.permute(nums)