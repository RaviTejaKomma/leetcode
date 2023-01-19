__author__ = 'Ravi Teja Komma'


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j) - ord('a')] += 1
            hash_map[tuple(count)] = [i] + hash_map.get(tuple(count), [])
        return hash_map.values()