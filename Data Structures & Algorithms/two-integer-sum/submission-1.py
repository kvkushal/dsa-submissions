class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d=[]
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    d.append(i)
                    d.append(j)
                    return d