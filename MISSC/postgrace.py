def get_largest_numbers(number,n):
    number.sort()
    return number[-n:]

nums = [3,5,6,7,4,3,2,1,0,0,]

print(nums)
largest = get_largest_numbers(nums,1)
print(largest)