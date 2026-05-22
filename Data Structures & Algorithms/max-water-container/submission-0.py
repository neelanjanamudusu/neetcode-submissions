from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
         left = 0
         right = len(heights) - 1
         ans = 0
         while left < right:
             area = (right - left) * min(heights[left], heights[right])
             if area > ans:
                 ans = area
             if heights[left] < heights[right]:
                 left += 1
             else:
                 right -= 1
         return ans