def binary_search(my_list: list, item: int):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = my_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    print(binary_search(list(range(1, 41)), 15))

