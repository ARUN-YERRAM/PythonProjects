def func(nums,n):
    sum = 0
    for i in range(n-1,-1,-1):
        sum += nums[i]
    return sum

nums = []
n = int(input())

for i in range(n):
    ele = int(input())
    nums.append(ele)

num = func(nums,n)
print(num)