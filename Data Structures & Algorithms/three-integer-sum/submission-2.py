class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for idx, n in enumerate(nums):
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp == -n:
                    if [n, nums[l], nums[r]] not in result:
                        result.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif tmp < -n:
                    l += 1
                elif tmp > -n:
                    r -= 1

        return result
                
            