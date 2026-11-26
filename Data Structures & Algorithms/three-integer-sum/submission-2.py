class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for anchor in range(len(nums)):
            if anchor > 0 and nums[anchor] == nums[anchor - 1]:
                continue
            target = -nums[anchor]
            l = anchor + 1
            r = len(nums) - 1
            while l < r:
                # print("(", anchor, l, r, ")", "(", nums[anchor], nums[l], nums[r], ")", nums[anchor]+nums[l]+nums[r])
                triplet = [nums[anchor], nums[l], nums[r]]
                if nums[l] + nums[r] == target:
                    res.append(triplet)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res