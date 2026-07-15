class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for n in nums:
            table[n] = table.get(n, 0) + 1

        sorted_dict = dict(sorted(table.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict)
        result = []
        for idx, key in enumerate(sorted_dict):
            result.append(key)
            if idx == k - 1:
                break
        
        return result