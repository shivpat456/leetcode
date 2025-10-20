import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_k = float('inf')
        while left <= right:
            mid_k = (left + right) // 2 

            sum_hours = 0
            for pile in piles:
                sum_hours += math.ceil(pile / mid_k)
            
            if sum_hours > h:
                left = mid_k + 1
            else:
                min_k = min(min_k, mid_k)
                right = mid_k - 1

        return min_k

