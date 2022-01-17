# def unique_in_order(iterable):
#     my_list = []
#     for i in range(1, len(iterable)):
#         if iterable[i] != iterable[i - 1]:
#             my_list.append(iterable[i - 1])
#     my_list.append(iterable[-1])
#     return my_list

def unique_in_order(iterable):
    last_char = ''
    my_list = []
    for letter in iterable:
        if str(letter) != last_char:
            last_char = str(letter)
            my_list.append(letter)
    return my_list


print(unique_in_order('AAAABBBCCDAABBB'))


if __name__ == '__main__':
    assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
    assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
