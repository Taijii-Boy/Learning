import time
from threading import Thread, Event

# ==========================================================
# def countdown(n):
#     while n > 0:
#         print('T-minus ', n)
#         n -= 1
#         time.sleep(1)
#
#
# t1 = Thread(target=countdown, args=(5,))
# t2 = Thread(target=lambda: print('Выполняю какую-то задачу'))
#
# t1.start()
# t1.join()
# t2.start()
# ==========================================================

# class CountdownTask:
#     def __init__(self):
#         self._running = True
#
#     def terminate(self):
#         self._running = False
#
#     def run(self, n):
#         while self._running and n > 0:
#             print('T-minus ', n)
#             n -= 1
#             time.sleep(1)
#
#
# c = CountdownTask()
# t = Thread(target=c.run, args=(5,))
# t.start()
# c.terminate()
# t.join()
# ============================================================

# Код для выполнения в независимом потоке
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

# Создать объект события, который будет использован для сигнала о запуске
started_evt = Event()
# Запустить поток и передать событие запуска
print('Launching countdown')
t = Thread(target=countdown, args=(5,started_evt))
t.start()
# Ждать запуска потока
started_evt.wait()
print('countdown is running')
