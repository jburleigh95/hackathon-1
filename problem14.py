count = int(input("How many numbers?: "))

nums = [int(input(f"Enter Number {num + 1}: ")) for num in range(count)]
even_nums = [num for num in nums if num % 2 == 0]
even_sum = sum(even_nums)

print(f"The sum of all the even numbers is: {even_sum}")