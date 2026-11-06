class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c)-ord('a')] += 1
            sublists[tuple(counts)].append(s)
        return [sublist for sublist in sublists.values()]