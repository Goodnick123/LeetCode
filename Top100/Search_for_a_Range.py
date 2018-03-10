class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left =0
        right=len(nums)-1
        arr=[-1,-1]
        while(left<=right):
            mid=int((left+right)/2)
            if(nums[mid]==target):
                while(mid-1>=0 and nums[mid-1]==target):
                    mid-=1
                arr[0]=mid
                tmp =mid
                while(mid+1<=right and nums[mid+1]==target):
                    mid+=1
                arr[1]=mid
                break

            elif nums[mid]<target:
                left =mid+1
            else:
                right = mid-1
        return arr
s=Solution()
nums=[5]
target =5
print(s.searchRange(nums,target))

