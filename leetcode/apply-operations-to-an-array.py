class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        ans = [nm for nm in nums if nm != 0]
        ans += [0] * (len(nums)-len(ans))
        return ans
