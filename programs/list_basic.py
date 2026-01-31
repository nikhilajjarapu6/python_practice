nums = [10, 20, 10, 30, 20]

#remove duplicates and keep order
result = []

for n in nums:
    if n not in result:
        result.append(n)

print(result)  # [10, 20, 30]

#find max number
nums = [5, 9, 2, 15, 1]
large=nums[0]
for n in nums :
    if n>large:
        large=n
print(large)

#separate even aand odd
nums = [1,2,3,4,5,6]
even=[]
odd=[]
for n in nums:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
print(even)
print(odd)

#reverse list 
rev=[]
for i in range(len(nums)-1, -1,-1):
    rev.append(nums[i])

print(rev) 
if(nums==rev):
    print("palindrome")
else:
    print("not palindrome")
rev = nums[::-1]
print(rev)
rev = list(reversed(nums))
print(rev)
print(max(nums))
print(sum(nums))

#find second largest number
nums = [5, 9, 2, 15, 1] 
first = second = nums[0]
for n in nums:
    if n > first:
        second = first
        first = n
    elif first > n > second:
        second = n                          
print("Second largest number is:", second)  



