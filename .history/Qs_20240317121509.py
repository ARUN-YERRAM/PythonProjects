-- nums = []
-- n = int(input())

-- for i in range(n):
--     ele = int(input())
--     nums.append(ele)
    
def func(nums,n):
    sum = 0
    for i in range(n):
        sum += nums[i]
    return sum

num = func(nums,n)
print(num)

nums = []
n = int(input())

for i in range(n):
    ele = int(input())
    nums.append(ele)
    