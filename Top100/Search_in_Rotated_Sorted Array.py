class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid =int((left+right)/2)
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if nums[mid]>=target and nums[left]<=target:
                    right=mid-1
                else:
                    left =mid+1
            else:
                if nums[right]>=target and nums[mid]<=target:
                    left=mid+1
                else:
                    right =mid-1
        return -1
nums=[1,3,5]
target =0
demo =Solution()
print(demo.search(nums,target))