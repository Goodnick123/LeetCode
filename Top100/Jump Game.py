class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==None:return True
        dp=[0]*len(nums)
        dp[0]=1
        for i in range(0,len(nums)):
            if dp[i]==1:
                for j in range(0,nums[i]+1):
                    if i+j<len(nums):
                        dp[i+j]=1
                    else:
                        break
            else:
                break
        return dp[len(nums)-1]==1

    def jump(self,nums):
        max1=0
        for i in range(0,len(nums)):
            if i>max1:return False
            max1 =max(nums[i]+i,max1)
        return True
arr =[2,3,1,1,4]
demo =Solution()
print(demo.jump(arr))
