class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            tmp = target - numbers[i]  # 2
            left = i + 1  # 1
            right = len(numbers) - 1  # 3
            while left <= right:
                mid = (left + right) // 2  # 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                if numbers[mid] > tmp:
                    right = mid - 1  # 1
                else:
                    left = mid + 1
        return []