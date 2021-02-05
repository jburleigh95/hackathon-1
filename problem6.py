import math


def reverse_round():
    user_input = input("Enter a decimal number to be rounded in reverse: ")
    nums = user_input.split(".")
    num_as_float = float(user_input)
    dec_value = num_as_float % float(nums[0])
    if dec_value >= 0.5:
        result = math.floor(num_as_float)
        direction = "down"
    else:
        result = math.ceil(num_as_float)
        direction = "up"
    print(f"{num_as_float} was rounded {direction} to {result}")


reverse_round()
