class Solution:
    def primeFac(self, n):
        ans = []
        i = 2

        while i * i <= n:
            if n % i == 0:
                ans.append(i)

                while n % i == 0:
                    n = n // i

            i += 1

        if n > 1:
            ans.append(n)

        return ans