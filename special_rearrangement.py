def special_rearrangement(nums):
    arranged_odds = []
    arranged_evens = []
    for i in nums:
        if i % 2 == 0:
            arranged_evens.append(i)
        else:
            arranged_odds.append(i)

    rearranged_list = arranged_evens + arranged_odds
    return print(f"The new arranged list of numbers = {rearranged_list}")


# Entering list of numbers

numbers = int(input("Enter how many numbers do you want to arrange:  "))
unarranged_numbers = []
for i in range(numbers):
    price = int(input(f"Enter number {i + 1}: "))
    unarranged_numbers.append(price)

print(f"The unarranged list of numbers is= {unarranged_numbers}")
special_rearrangement(unarranged_numbers)
