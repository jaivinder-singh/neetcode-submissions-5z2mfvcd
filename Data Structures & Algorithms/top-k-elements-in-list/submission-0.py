class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        store = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            if num not in store:
                store[num] = 1
            
            else:
                store[num] += 1

        for num,count in store.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res