my_list = [1, 23, 45, 645, 23, 434, 1, 5]


def get_some_list(some_list: list) -> list | None:
    if len(some_list) == len(set(some_list)):
        return None  # Списки одинаковы

    result_list = []
    for a, some_list_a in enumerate(some_list):
        for b, some_list_b in enumerate(some_list[a + 1:]):
            if some_list_b == some_list_a:
                result_list.append(some_list_a)
    return result_list


print(get_some_list(my_list))
