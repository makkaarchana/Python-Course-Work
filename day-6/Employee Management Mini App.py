# Taking employee details
emp_id = int(input("Enter employee ID: "))
name = input("Enter employee name: ")
department = input("Enter department: ")
salary = float(input("Enter monthly salary: "))

# Display employee details
print("\n--- Employee Details ---")
print("Employee ID:", emp_id)
print("Employee Name:", name)
print("Department:", department)
print("Monthly Salary:", salary)

# Calculate annual salary
annual_salary = salary * 12
print("Annual Salary:", annual_salary)

# Update salary
new_salary = float(input("\nEnter new salary: "))
salary = new_salary

print("\nSalary updated successfully!")

# Display updated employee details
print("\n--- Updated Employee Details ---")
print("Employee ID:", emp_id)
print("Employee Name:", name)
print("Department:", department)
print("Updated Monthly Salary:", salary)

# Calculate updated annual salary
annual_salary = salary * 12
print("Updated Annual Salary:", annual_salary)