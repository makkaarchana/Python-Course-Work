print("------scholarship-------")

n=int(input("enter  your age: "))
p=int(input("enter percentage: "))
i=int(input(" enter Family annual income: "))

if n >= 18 and n <= 25 and p >= 85 and i <= 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")