print("------ Job Eligibility Verification ------")

age = int(input("Enter candidate age: "))
qualification = input("Enter educational qualification: ")
percentage = float(input("Enter percentage: "))
experience = int(input("Enter years of experience: "))
skills = input("Do you have required technical skills (yes/no): ")

if age >= 21 and qualification.lower() == "degree" and percentage >= 60 and (experience >= 2 or skills.lower() == "yes"):
    print("Congratulations! You are eligible for the job.")
else:
    print("Sorry! You are not eligible for the job.")