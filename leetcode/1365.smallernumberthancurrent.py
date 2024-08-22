from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        refr = sorted(nums)
        ans = [bisect_left(refr, i) for i in nums]
        return ans
        
        
