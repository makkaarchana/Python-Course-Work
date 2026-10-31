em_id=input("enter your id:")
name=input("enter your name:")
dept=input("enter your dept:")
sal=float(input("enter your sal:"))
#calculating hra and da
hra=sal*20/100
da=sal*10/100
#calculating gross salary
gross_sal=sal+hra+da

print("----salary details---")
print("name: ",name)
print("dept:",dept)
print("em_id: ",em_id)
print("hra: ",hra)
print("da: ",da)
print("gross_sal: ",gross_sal)
