# test.assert_equals(persistence(39), 3)
# test.assert_equals(persistence(4), 0)
# test.assert_equals(persistence(25), 2)
# test.assert_equals(persistence(999), 4)
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)


# def persistence(n):
#     if n < 10:
#         return 0
#     string_digits = str(n)
#     res = 1
#     while len(string_digits) > 1:
#         for digit in string_digits:
#             res = res * int(digit)
#         string_digits = str(res)
#     return res






print(persistence(39))
