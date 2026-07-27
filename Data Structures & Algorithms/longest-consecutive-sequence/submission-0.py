class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = Counter(nums)
        maxlen = 0
        for n in nums:
            tmp_len = 1
            if n - 1 not in table:
                i = 1
                while True:
                    if n + i in table:
                        tmp_len += 1
                    else:
                        maxlen = max(maxlen, tmp_len)
                        break
                    i += 1

        return maxlen