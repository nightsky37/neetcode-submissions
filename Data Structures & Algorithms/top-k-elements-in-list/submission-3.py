class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for n in nums:
            table[n] = table.get(n, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]
        for key, value in table.items():
            buckets[value].append(key)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]
                
