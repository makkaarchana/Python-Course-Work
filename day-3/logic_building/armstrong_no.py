class Solution:
    def armstrongNumber (self, n):
        # code here
        k=n
        rev=0
        while n>0:
            ld=n%10
            rev=rev+ld**3
            n=n//10
            
        return rev==k