





# def find_combinations(arrays, target_sum, current_sum=0, array_index=0, combination=[]):
#     if array_index == len(arrays):
#         if current_sum == target_sum:
#             print(combination)
#         return
#
#     # 从当前数组选取一个数字
#     for num in arrays[array_index]:
#         new_combination = combination + [num]
#         new_sum = current_sum + num
#         if new_sum <= target_sum:
#             find_combinations(arrays, target_sum, new_sum, array_index + 1, new_combination)
#
#     # 不选取当前数组中的数字，继续递归
#     # find_combinations(arrays, target_sum, current_sum, array_index + 1, combination)
#
#
# #
# # def bianLi(arrays, target_sum, current_sum=0, array_index=0, combination=[]):
# #     for
#
#
# arrays = [[2, 3, 5, 6], [4, 5, 7], [2, 5, 6]]
# target_sum = 12
# print("所有的组合方式为：")
# find_combinations(arrays, target_sum)
#
#
#
