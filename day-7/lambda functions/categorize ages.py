age_category = lambda age: "Minor" if age < 18 else "Adult"

age = int(input("Enter your age: "))

print(age_category(age))