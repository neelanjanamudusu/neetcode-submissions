from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in ans:
                        ans.append(triplet)
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans