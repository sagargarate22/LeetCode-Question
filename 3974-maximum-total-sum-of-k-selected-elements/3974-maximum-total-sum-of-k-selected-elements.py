class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)

        nums = nums[0:k]
        res = 0
        for num in nums:
            if mul > 0:
                res += num * mul
            else:
                res += num
            mul -= 1
        return res