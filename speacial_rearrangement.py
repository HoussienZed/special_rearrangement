def special_rearrangement(nums):
    for i in nums:
        if i % 2 != 0:
            nums.append(i)  # appending i as the last element of the list
            nums.remove(i)  # removes the first ocuurence of i

    return nums
