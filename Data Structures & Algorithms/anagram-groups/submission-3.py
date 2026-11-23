class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        ord_a = ord('a')
        for word in strs:
            counts = [0] * 26
            for char in word:
                idx = ord(char) - ord_a
                counts[idx] += 1
            hashmap_key = tuple(counts)
            # sorted_word = ''.join(sorted(word) )
            if not hashmap_key in res:
                res[hashmap_key] = [word]
            else:
                res[hashmap_key].append(word)
        return list(res.values())