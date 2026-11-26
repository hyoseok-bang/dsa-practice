class Solution:
    def maxArea(self, heights: List[int]) -> int:
        amount = 0
        l = 0
        r = len(heights) - 1
        for _ in range(len(heights)):
            l_height = heights[l]
            r_height = heights[r]
            height = min(l_height, r_height)
            width = r - l
            curAmount = height * width
            # print(l, r, l_height, r_height, height, width, curAmount)
            if curAmount > amount:
                amount = curAmount
            if l_height == height:
                l += 1
            else:
                r -= 1
        return amount
