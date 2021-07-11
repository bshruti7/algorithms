from collections import deque,defaultdict


def get_digit(num, lsb_index):
    while num:
        if lsb_index == 1:
            remainder = num % 10
            num = num / 10
            return remainder
        else:
            num = num // 10
            lsb_index -= 1
    return 0


def radix_sort(my_array):

    # find max number
    max_num = max(my_array)
    max_digits = len(str(max_num))
    temp = my_array.copy()
    buckets = defaultdict(deque)

    for digit in range(1, max_digits+1):
        for num in temp:
            digit_at_index = get_digit(num, digit)
            buckets[digit_at_index].append(num)

        temp = []
        for i in range(10):
            for _ in range(len(buckets[i])):
                temp.append(buckets[i].popleft())

    return temp


my_array = [3, 44, 38, 5, 47, 37,15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(f'Input array:{my_array}')
print(f'Output array: {radix_sort(my_array)}')

