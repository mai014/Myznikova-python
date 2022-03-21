nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new_list1 = [elem[i] for elem in nice_list for i in range(0, 3)]
new_list2 = [elem[i] for elem in new_list1 for i in range(0, 3)]
print('Внешний список: ', new_list2)