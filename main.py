import threading
import math

numbers = list(range(1, 1000001))

cift_sayilar = []
tek_sayilar = []
asal_sayilar = []


def process_numbers(start, end, result_list, condition_func):
    for i in range(start, end):
        number = numbers[i]

        if condition_func(number):
            result_list.append(number)



def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

threads = []

for i in range(4):
    start_index = i * (len(numbers) // 4)
    end_index = (i + 1) * (len(numbers) // 4)

    thread = threading.Thread(target=process_numbers,args=(start_index, end_index, cift_sayilar, lambda x: x % 2 == 0))
    threads.append(thread)
    thread.start()

for i in range(4):
    start_index = i * (len(numbers) // 4)
    end_index = (i + 1) * (len(numbers) // 4)

    thread = threading.Thread(target=process_numbers,args=(start_index, end_index, tek_sayilar, lambda x: x % 2 != 0))
    threads.append(thread)
    thread.start()

for i in range(4):
    start_index = i * (len(numbers) // 4)
    end_index = (i + 1) * (len(numbers) // 4)

    thread = threading.Thread(target=process_numbers,args=(start_index, end_index, asal_sayilar, is_prime))
    threads.append(thread)
    thread.start()

for thread in threads: thread.join()

print("Çift sayılar:", cift_sayilar)
print("Tek sayılar:", tek_sayilar)
print("Asal sayılar:", asal_sayilar)

