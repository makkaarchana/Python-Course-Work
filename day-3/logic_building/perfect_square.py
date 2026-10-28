class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        # code here
        
                i = 0

                while i * i < n:
                    i += 1

                return i * i == n