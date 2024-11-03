def special_rearrangement(nums):
    for i in nums:
        if i % 2 != 0:
            nums.append(i)  # appending i as the last element of the list
            nums.remove(i)  # removes the first ocuurence of i

    return print(f"The new arranged list of numbers = {nums}")


# Entering list of numbers

numbers = int(input("Enter how many numbers do you want to arrange:  "))
unarranged_numbers = []
for i in range(numbers):
    price = int(input(f"Enter number {i + 1}: "))
    unarranged_numbers.append(price)

print(f"The unarranged list of numbers is= {unarranged_numbers}")
special_rearrangement(unarranged_numbers)
