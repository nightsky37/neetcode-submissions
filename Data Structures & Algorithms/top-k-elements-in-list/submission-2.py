class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for n in nums:
            table[n] = table.get(n, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]
        for key, value in table.items():
            buckets[value].append(key)

        counted = 0
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                counted += 1
            if counted == k:
                break
        
        return result
