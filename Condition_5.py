# condition 1: the number should be divisible by 5, print those number
nums = [12, 75, 150, 180, 145, 525, 50]
for n in nums:
    if n % 5 == 0:
        print(n)

# condition 2: if the number is greater than 150, skip it and move to next number
nums = [12, 75, 150, 180, 145, 525, 50]
for i in nums:
    if i >= 150:
        continue
    print(i)
um
# condition 3: if the number is greater than 500, stop the loop
nums = [12, 75, 150, 180, 145, 525, 50]
for i in nums:
    if i > 500:
        break
    print(i)











