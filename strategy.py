chess_pieces = {
    0:"None",
    1:"Red General",
    2:"Red Benteng",
    3:"Red Kuda",
    4:"Red Gajah",
    5:"Red Mentri",
    6:"Red Cannon",
    7:"Red Soldier",
    8:"Black General",
    9:"Black Benteng",
    10:"Black Kuda",
    11:"Black Gajah",
    12:"Black Mentri",
    13:"Black Cannon",
    14:"Black Soldier",
}

# example1 = [
#     [2,  0, 0,  0,  0, 0, 14,  0,  2,  0],
#     [0,  0, 6,  0,  0, 0,  0, 14,  0,  9],
#     [0, 14, 0,  7,  0, 7,  0,  0,  3,  0],
#     [0, 10, 4,  0,  9, 0,  5,  0, 11,  0],
#     [1,  0, 0,  7,  0, 0,  0,  4,  0,  3],
#     [0,  0, 8,  0,  0, 0,  0,  0,  0,  0],
#     [5, 10, 0, 13,  0, 0, 14,  0, 12,  0],
#     [0,  0, 6,  0, 12, 7,  0, 13,  0, 11],
#     [0,  0, 0,  7,  0, 0, 14,  0,  0,  0]
# ]
# target = [
#     [2, 0, 0, 7, 0, 0, 14,  0, 0,  9],
#     [3, 0, 6, 0, 0, 0,  0, 13, 0, 10],
#     [4, 0, 0, 7, 0, 0, 14,  0, 0, 11],
#     [5, 0, 0, 0, 0, 0,  0,  0, 0, 12],
#     [1, 0, 0, 7, 0, 0, 14,  0, 0,  8],
#     [5, 0, 0, 0, 0, 0,  0,  0, 0, 12],
#     [4, 0, 0, 7, 0, 0, 14,  0, 0, 11],
#     [3, 0, 6, 0, 0, 0,  0, 13, 0, 10],
#     [2, 0, 0, 7, 0, 0, 14,  0, 0,  9]
# ]

example1 = [
    2,  0, 0,  0,  0, 0, 14,  0,  2,  0,
    0,  0, 6,  0,  0, 0,  0, 14,  0,  9,
    0, 14, 0,  7,  0, 7,  0,  0,  3,  0,
    0, 10, 4,  0,  9, 0,  5,  0, 11,  0,
    1,  0, 0,  7,  0, 0,  0,  4,  0,  3,
    0,  0, 8,  0,  0, 0,  0,  0,  0,  0,
    5, 10, 0, 13,  0, 0, 14,  0, 12,  0,
    0,  0, 6,  0, 12, 7,  0, 13,  0, 11,
    0,  0, 0,  7,  0, 0, 14,  0,  0,  0
]

target = [
    2, 0, 0, 7, 0, 0, 14,  0, 0,  9,
    3, 0, 6, 0, 0, 0,  0, 13, 0, 10,
    4, 0, 0, 7, 0, 0, 14,  0, 0, 11,
    5, 0, 0, 0, 0, 0,  0,  0, 0, 12,
    1, 0, 0, 7, 0, 0, 14,  0, 0,  8,
    5, 0, 0, 0, 0, 0,  0,  0, 0, 12,
    4, 0, 0, 7, 0, 0, 14,  0, 0, 11,
    3, 0, 6, 0, 0, 0,  0, 13, 0, 10,
    2, 0, 0, 7, 0, 0, 14,  0, 0,  9
]


count=0
for i in range(len(example1)):
    if example1[i]==target[i]:
        count += 1
        continue
    else: 
        target_index = example1[i:].index(target[i]) + count
        example1[i], example1[target_index] = example1[target_index],example1[i]
        x = i // 10
        y = (i - x*10)%10
        x2 = target_index // 10
        y2 = (target_index - x*10)%10
        print((x2,y2),"swap",(x,y)) 
        # print(target_index)
        count += 1

if target==example1:
    print("mission finished")

print(-1//10, 8//9)