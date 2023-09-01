list1 = [1,2,3,4,3,5,6,3]
correct_location = [2,4]

target = list1.index(3)
# print(target)
while target in correct_location:
    # print(list1[target+1:])
    target = list1[target+1:].index(3) + target + 1
    # print(target)

print(target)