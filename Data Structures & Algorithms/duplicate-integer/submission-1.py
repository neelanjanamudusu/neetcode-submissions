class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = set()

        for num in nums:

            if num in i:

                return True

            i.add(num)

        return False
        