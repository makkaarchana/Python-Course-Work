class Solution:
    def countDigits(self, n: int) -> int:
        # Code here
        count=0
        if n == 0:
            count = 1
        else:
            while n>0:
                n=n//10
                count=count+1
        return count