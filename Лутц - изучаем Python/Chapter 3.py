# s = "Hello, my name is Aleksandr"

# 1.a
# for letter in s:
#     print(ord(letter))

# 1.б
# code_list = []
# for letter in s:
#     code_list.append(ord(letter))
# print(sum(code_list))

# # 1.в
# x = []
# for letter in s: x.append(ord(letter))
# print(x)
# new_s = [ord(letter) for letter in s]
# print(new_s)
# print(map(ord, s))
# print(list(map(ord, s)))
# print([ord(c) for c in s])
# --------------------------------------------------------------------------------
# 3
# d = {'ha': 2, 'd': 13, 'c': 4, 'f': 8, 'g': 9}

# keys = list(d.keys())
# keys.sort()
# for key in keys:
#     print(f'{key} > {d[key]}')
#
# for key in sorted(d):
#     print(f'{key} > {d[key]}')

# --------------------------------------------------------------------------------
# 4

# l = [1, 2, 4, 8, 16, 32, 64]
# x = 5
# found = False
# i = 0
# while not found and i < len(l):
#     if 2 ** x == l[i]:
#         found = True
#     else:
#         i = i + 1
#     if found:
#         print('at index', i)
#     else:
#         print(x, 'not found')

# l = [1, 2, 4, 8, 16, 32, 64]
# x = 5
# i = 0
# while i < len(l):
#     if 2**x == l[i]:
#         print('at index', i)
#         break
#     i += 1
# else:
#     print(x, 'not found')

# l = [1, 2, 4, 8, 16, 32, 64]
# x = 5
# if 2**x in l:
#     print(f'{2**x} was found at {l.index(2**x)}')
# else:
#     print(2**x, 'not found')

x = 5
l = list(map(lambda x: 2 ** x, range(7)))
print(l)
if (2 ** x) in l:
    print((2 ** x), 'was found at', l.index(2 ** x))
else:
    print(x, 'not found')