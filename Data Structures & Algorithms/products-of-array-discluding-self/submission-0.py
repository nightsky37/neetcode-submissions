class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [0] * len(nums), [0] * len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]
        
        result = [0] * len(nums)
        result[0] = suffix[1]
        result[-1] = prefix[-2]
        print(prefix)
        print(suffix)
        for i in range(1, len(nums) - 1):
            result[i] = prefix[i - 1] * suffix[i + 1]

        return result