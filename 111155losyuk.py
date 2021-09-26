nums = input().split()
nums = [int(item) for item in nums]
for i in nums:
    if -nums[i] == 0:
        print(i, nums.index(-nums[i]))
    else:
        if -nums[i] in nums:
            print(i, nums.index(-nums[i]))
        break

