nums = [10, 20, 30]

def sumavg(nums):
    total = 0 
    for n in nums:
        total = total + n
    
    return (total, total/len(nums))


print(sumavg(nums))