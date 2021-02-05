def calculate_age():
    date_input = input("Enter the date for which you would like to calculate the person's age (Format: DD/MM/YYYY): ")
    date_of_birth = input("Enter the person's date of birth (Format: DD/MM/YYYY): ")
    date = convert_to_nums(date_input)
    birth_date = convert_to_nums(date_of_birth)
    age = date["year"] - birth_date["year"]
    if date['day'] < birth_date['day'] and date['month'] <= birth_date['month']:
        age -= 1
    elif date['month'] < birth_date['month']:
        age -= 1
    print(age)


def convert_to_nums(date):
    date_list = date.split("/")
    date_dict = {
        "day": int(date_list[0]),
        "month": int(date_list[1]),
        "year": int(date_list[2]),
    }
    return date_dict


calculate_age()