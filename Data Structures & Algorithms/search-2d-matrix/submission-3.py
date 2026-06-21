class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=-1
        nums=matrix
        m=len(nums)
        n=len(nums[0])
        l=0
        r=m-1
        while l<=r:

            mid=(l+r)//2

            if nums[mid][0]<=target<=nums[mid][n-1]:

                row=mid
                left=0
                right=n-1
                while left<=right:
                    
                    mid_inner=(left+right)//2
                    if nums[row][mid_inner]==target:
                        return True
                    elif nums[row][mid_inner]<target:
                        left=mid_inner+1
                    else:
                        right=mid_inner-1
                return False

            elif nums[mid][0]>target:
                r=mid-1

            else:
                l=mid+1

        return False
        