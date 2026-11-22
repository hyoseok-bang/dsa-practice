class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, n in enumerate(nums):
            lookup[n] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in lookup and i != lookup[diff]:
                return sorted([i, lookup[diff]]) 