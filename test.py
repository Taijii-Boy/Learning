def get_money():
    money_summ = 0
    for day_pay in range(1, 366):
        money_summ += day_pay
        print(day_pay)
    return money_summ

print(get_money())

