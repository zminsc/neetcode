class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for num, freq in c.items():
            if freq > len(nums) // 2:
                return num
        return -1