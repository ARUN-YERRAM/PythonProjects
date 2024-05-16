def func(nums,n):
    sum = 0
    for i in range(n):
        sum += nums[i]
    return sum


nums = []
n = int(input())

for i in range(n,0,-1):
    ele = int(input())
    nums.append(ele)
    

num = func(nums,n)
print(num)