class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r, ans = 0, len(nums) - 1, len(nums)
        
        while l <= r:
            if nums[r] == val:
                r -= 1
                ans -= 1
                continue
            if nums[l] == val:
                swp = nums[l]
                nums[l] = nums[r]
                nums[r] = swp
                r -= 1
                ans -= 1
            l += 1
        
        return ans