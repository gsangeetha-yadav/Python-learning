# common elements between two sets
set1 = {1,2,3,4,5,6}
set2 = {1,6,18,98,9}
result = set1 & set2
print(result)

# Remove duplicate from user list
lst = [1,2,3,6,7,1,2]
nums = set(lst)
print(nums)

# mini shopping cart
bill = ["sugar","Bru","clothes","hair band","chocolate"]
bill.append("books")
bill.remove("hair band")
print(bill)

# set operations
set1 = {1,2,3,4,54,6,3}
set2 = {1,3,4,5,6,3,9,10}
result = set1 & set2
result1 = set1 | set2
result2 = set1 - set2
print(result)
print(result1)
print(result2)

# tuple packing and unpacking
student = ("sangeetha",18,"CSE")
name , age , course = student
print(name)
print(age)
print(course)
