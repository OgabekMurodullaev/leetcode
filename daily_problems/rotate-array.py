from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)
        return nums