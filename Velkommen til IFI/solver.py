import sys

nums = []
o = open("input", "r")
for line in o.readlines():
    nums.append(int(line.strip()))

n = len(nums)
numSwaps = 0

for i in range(n-1):
    for j in range(0, n-i-1):

        # traverse the numsay from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if nums[j] > nums[j + 1] :
            numSwaps += 1
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(numSwaps)
