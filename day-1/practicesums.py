arr=[5,10,15,20]
total=0
for i in range (len(arr)):
    total=total+arr[i]
print(total)


#FIND LARGEST NUMBER
arr=[4,5,2,7]
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)

#FIRST 10 FIBONACCI NUMBERS
a=0
b=1
n=10
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c


#REVERSE A STRING
s=("python")
rev=" "
for ch in s:
    rev=ch+rev
print(rev)

#STRING IS PALINDROME 
s=("madam")
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")


