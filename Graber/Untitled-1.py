   
#! /usr/bin/env python3


# l1 = []
# for int in range(1,101):
#     l1.append(int)
# # print(l1)
# li_revers = (int for int in reversed(range(1, 100_00_00_00)))
# # print(li_revers)
# li_100500 = ()
# for i in li_revers:
#     if i == 100500:
#         li_100500 = i
# print(li_100500)

# li_s = [5,4,3,2,1]
# li1 = sorted(li_s, reverse=False)
# print(li1)


# create generator of nuimbers() and numbers in 1 - 5000 
# add to list each 100th
# prunt list backwords
# li_elem = []
# for elem in range(0, 5001, 100):
#     li_elem.append(elem)
# print(li_elem)

li_elem = (elem for elem in range(0, 5001, 100))
# print(li_elem)
elem_data = []
for elem in li_elem:
    elem_data.append(elem)
    # print(elem)
# print(elem_data)
reversed_elem = [index for index in reversed(elem_data) if index % 6 == 0]
print(reversed_elem)
