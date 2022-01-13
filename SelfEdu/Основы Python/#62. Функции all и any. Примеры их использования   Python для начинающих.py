# a = [0, 1, 2.5, "", "python", [], [1, 2], {}]
# # a = [True, True, True, True]

# All в виде цикла:
# all_res = True
# for x in a:
#     all_res = all_res and bool(x)

# Any в виде цикла:
# all_res = False
# for x in a:
#     all_res = all_res or bool(x)
#
# b = all(a)
# c = any(a)
# print(c)

# --------------------------------------------
# Крестики-нолики. Проверка победы
# p = ['x', 'x', 'o',
#      'o', 'o', 'o',
#      'x', 'o', 'x']

# row_1 = all(map(lambda x: x == 'x', p[:3]))
# row_2 = all(map(lambda x: x == 'x', p[3:6]))
# row_3 = all(map(lambda x: x == 'x', p[6:]))


# То же самое, но без дублирования кода:


# def true_x(a):
#     return a == 'x'
#
#
# row_1 = all(map(true_x, p[:3]))
# row_2 = all(map(true_x, p[3:6]))
# row_3 = all(map(true_x, p[6:]))
#
# col_1 = all(map(true_x, p[::3]))
# col_2 = all(map(true_x, p[1::3]))
# col_3 = all(map(true_x, p[2::3]))
#
# diag_1 = all(map(true_x, p[::4]))
# diag_2 = all(map(true_x, p[2:7:2]))
#
# print(any([row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2]))

# --------------------------------------------
# Минер
N = 10
P = [0] * (N * N)
P[4] = '*'
loss = any(map(lambda x: x == '*', P))
print(loss)
