nums=(10,30,20,40,50)
# nums[-1]=(60) cannot modify
list=list(nums)
list.append(60)
# list.remove(70)
nums=tuple(list)
print(list)
print(nums)
print(type(nums))