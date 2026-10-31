total=0
for i in range(1,6):
  name=input("enter the product name:")
  weight=float(input("enter product weight: "))
  price=float(input("enter product price: "))

  cost=weight*price

  print("product: ", name)
  print("total cost :",cost)

  total+=cost
print("final bill: ",total)