from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        swapped = False
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        for i in range(0, len(nums)-1):
            for j in range(0, len(nums)-i-1):
                if nums[j].bit_count() == nums[j+1].bit_count() and nums[j] > nums[j+1]:
                    swapped = True
                    swap(j, j+1)
            
            if not swapped:
                break
        
        for i in range(1, len(nums)):
            if (nums[i] < nums[i-1]):
                return False
        
        return True
