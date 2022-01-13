bad = ['a', 'b', 'c']
good = ['good']
#
# Моё решение
# def filter_words(text):
#     bad = [word for word in text.split() if word in bad_words]
#     good = [word for word in text.split() if word in good_words]
#     if not bad and good:
#         return "Тест пройден"
#     else:
#         return "Тест не пройден"
#
#
# # print(filter_words('a good ssd fdgfgk ffsd'))
#
#
# if __name__ == '__main__':
#     assert filter_words('a ssd fdgfgk ffsd') == "Тест не пройден"
#     assert filter_words('b sdlfk ksd good') == "Тест не пройден"
#     assert filter_words('ja ssd fdgfgk ffsd') == "Тест не пройден"
#     assert filter_words('ssd f11 dklfk good kffk') == "Тест пройден"

# ----------------------------------------------------------------------
# Не моё решение:
# def filter_words(text):
#     set_words = set(text.split())
#     if set_words.intersection(bad) == set() and set_words.intersection(good) != set():
#         return "Проверка пройдена"
#     return "Проверка не пройдена"
#
#
# print(filter_words('ssd a good fdgfgk ffsd'))
