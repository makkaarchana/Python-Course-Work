name=input("enter u r name:")
saving=float(input("enter your savings:"))
print("1.deposit money")
print("2.withdraw money")
print("3.check bank balance")
n=int(input("select any : "))

#for deposit
if n==1:
  a=float(input("enter deposit money:"))
  depo=saving+a
  print("money deposited",depo)
#for withdraw
elif n==2:
  b=int(input("enter withdraw amount:"))
  withdraw=saving-b
  print("withdraw successful",withdraw)
# to check balance
elif n==3:
   print("balance:",saving)
else:
  print("wrong option")
  
      