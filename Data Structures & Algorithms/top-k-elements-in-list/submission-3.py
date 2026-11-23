class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n not in hashmap.keys():
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        
        freqs = [(k, v) for k, v in hashmap.items()]
        freqs.sort(key=lambda x: x[1], reverse=True)
        return [k for k, v in freqs[:k]]