nums = [1, 2, 3, 4, 5, 6]

def retsqrs(nums):
    square_list = []
    for n in nums:
        if n % 2 == 0:
            square_list.append(n*n)

    return square_list

print(retsqrs(nums))