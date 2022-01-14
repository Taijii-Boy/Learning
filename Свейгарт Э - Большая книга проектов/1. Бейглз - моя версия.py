"""В дедуктивной логической игре «Бейглз» необходимо по подсказкам угадать секретное число из трех цифр. В ответ на
ваши попытки угадать игра выдает одну из трех подсказок: Pico, если вы угадали правильную цифру на неправильном месте,
Fermi, если в вашей догадке есть правильная цифра на правильном месте, и Bagels, если в догадке не содержится
правильных цифр. На угадывание секретного числа у вас десять попыток. """

import random


def check_input(number: str) -> str:
    while not number.isdigit():
        print("Неверный формат ввода! Введите число!")
        number = input()
    return number


def config_game() -> tuple:
    print('Число из скольких цифр будем угадывать: ')
    dig_length = check_input(input())
    print('Со скольки попыток попробуем угадать: ')
    max_gues = check_input(input())
    print()
    return dig_length, max_gues


def show_title_screen(dig_length: str):
    print(f'''Я загадываю число из {dig_length} цифр. Попробуй угадать!
    Когда я скажу:      Это значит:
    Pico                Одна цифра правильная, но не на своей позиции
    Fermi               Одна цифра правильная и на своей позиции
    Bagels              Все цифры не правильные ''')


def get_secret_number(length: str) -> str:
    digits = [x for x in '0123456789']
    random.shuffle(digits)
    secret_number = ''
    for i in range(int(length)):
        secret_number += digits[i]
    return secret_number


def show_number_guess(max_gues: str):
    print(f'''Я загадал число!
    У тебя есть {max_gues} попыток, чтобы отгадать. Удачи! ''')


def get_clue(number: str):
    pass


def repeat_game() -> bool:
    print('Хотите повторить еще раз? Введите y / n: ')
    answer = input().lower()
    return answer in ['y', 'yes', 'д', 'да']


def try_guess(guess: int, secret_num: str):
    print(f'Попытка № {guess}. Введите число:')
    answer_num = check_input(input())
    if answer_num == secret_num:
        print('Поздравляю! Ты угадал!')
    else:
        print('Не угадал!')


if __name__ == '__main__':
    current_guess = 1
    continue_game_flag = True

    digit_length, max_guesses = config_game()
    show_title_screen(digit_length)
    show_number_guess(max_guesses)

    while continue_game_flag:
        number = get_secret_number(digit_length)
        while current_guess <= int(max_guesses):
            try_guess(current_guess, number)
            current_guess += 1

        print('К сожалению, вы проиграли!')
        continue_game_flag = repeat_game()
        current_guess = 1



