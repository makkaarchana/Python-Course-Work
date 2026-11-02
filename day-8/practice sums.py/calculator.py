print("-------calculator---------")

a= int(input("enter a no: "))
b= int(input("enter b no: "))
print("1.addition")
print("2.subraction")
print("3.division")
print("4.floor division")
print("5.multiplication")
print("6.exponentiation")
n=int(input("select any one of them: "))

if n==1:
  print("add :", a+b)
elif n==2:
  print("sub: ",a-b)
elif n==3:
  print("div: ",a/b)
elif n==4:
  print("floor div: ",a//b)
elif n==5:
  print("multi:",a*b)
elif n==6:
  print("expo:",a**b)
else:
  print("invalid input")

