class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        array = [[] for n in range(len(nums) + 1)] 

        for i in nums:
            my_map[i] = 1 + my_map.get(i, 0)
        for i, c in my_map.items():
            array[c].append(i)

        res = []
        for i in range(len(array) -1, 0, -1):
            for n in array[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    