import datetime
import random


def input_days_count() -> int:
    while True:
        count = int(input("How many birthdays shall i generate? (Max 100) "))
        if count > 100 or count < 0:
            print("Вы должны ввести положительное целое число не больше 100")
        else:
            return count


def generate_birthdays(birth_count: int) -> list:
    start_day = datetime.date(2021, 1, 1)
    birthdays = []
    for days in range(birth_count):
        random_day = datetime.timedelta(random.randint(0, 364))
        birthdays.append(start_day + random_day)
    return birthdays


def dates_to_string_list(birthdays: list) -> list:
    return [f"{day:%b %d}" for day in birthdays]


def get_multi_days(birthdays: list) -> list:
    multiple_days = []
    for day in birthdays:
        if birthdays.count(day) > 1:
            multiple_days.append(day)

    return list(set(multiple_days))


def show_single_birthdays(birthdays: list):
    multiple_days = get_multi_days(birthdays)
    if multiple_days:
        print(f'In this simulation, multiple people have a birthday on: {", ".join(list(multiple_days))}')
    else:
        print("No multiple birthdays in this simulation")


def get_result_of_simulation(birth_count: int):
    birthdays = generate_birthdays(birth_count)
    multiple_days = get_multi_days(birthdays)
    return True if multiple_days else False


def show_result(result_counter: int, gen_count: int):
    print(f"""
    Out of 100,000 simulations of {gen_count} people, there was a matching birthday
    in that group {result_counter} times. This means that {gen_count} people have a 
    {result_counter / 100_000:.2%} chance of having a matching birthday in their group. 
    That's probably more than you would think!""")


if __name__ == '__main__':
    generate_count = input_days_count()
    birthdays_list = generate_birthdays(generate_count)
    birthdays_list = dates_to_string_list(birthdays_list)
    show_single_birthdays(birthdays_list)

    print(f"Let's run 100_000 simulations for {generate_count} people")
    input("Press Enter to begin...")

    multiple_days_counter = 1
    for simulation in range(0, 100_000):
        if get_result_of_simulation(generate_count):
            multiple_days_counter += 1
        if simulation % 10000 == 0:
            print(f"{simulation:,}'s run")
        counter_of_multiple_days = 1

    show_result(multiple_days_counter, generate_count)
