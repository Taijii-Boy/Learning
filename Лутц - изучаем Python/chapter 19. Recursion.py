# def mysum(L):
#     print(L)
#     if not L:
#         return 0
#     else:
#         return L[0] + mysum(L[1:])
# -----------------------------------------------------------------
#
# def mysum(L):
#     return L[0] if len(L) == 1 else L[0] + mysum(L[1:])

# print(mysum([1, 2, 3, 4]))
# print(mysum(['a', 'b', 'c', 'd']))
# # -----------------------------------------------------------------
#
# def mysum(L):
#     first, *rest = L
#     return first if not rest else first + mysum(rest)
#
# print(mysum(['a', 'b', 'c', 'd']))
# -----------------------------------------------------------------
# Косвенная рекурсия
def mysum(L):
    if not L: return 0
    return nonempty(L)


def nonempty(L):
    return L[0] + mysum(L[1:])

print(mysum([1, 2, 3, 4, 5, 6, 7]))