first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
age = int(input("Enter your age: "))
marital_status = input("Enter your marital status (Single/Married): ").lower()
sex = input("Enter your sex (Male/Female): ").lower()

titles = ["Miss", "Master", "Mrs", "Mr"]

if sex == 'male':
    if age < 18:
        title = "Master"
    else:
        title = "Mr."
else:
    if marital_status == 'single':
        title = "Miss"
    else:
        title = "Mrs."

print(f"Dear {title} {first_name} {last_name}")
