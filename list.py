nums = [70,10,20,30,40,60,50]
nums2=list((100,200,300,400,500))
print(nums)
print(type(nums))  #type of datatype
print(len(nums))  #length of list
nums.insert(6,80)  #adds item at certain index place
nums.append(90)  #adds item at end of the list
# nums.extend(nums2)  #adds another list at end of the list
nums[5:]=[50,60]
# nums[:-1]=[80]
# nums.remove(90)  #removes specified item
# nums.pop()  #removes last item
nums.sort(reverse=False)
print(nums)
nums.reverse()
print(nums)
nums.clear()
print(nums)
del nums
# print(nums)


