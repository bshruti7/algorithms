# set the first element as minimum element
# find real minimum element
# swap with minimum element
# proceed with setting second element as new minimum

def selection_sort(arr):

    min_elem_index = 0

    while min_elem_index < len(arr)-1:
        found_min_elem_index = None
        min_elem = arr[min_elem_index]
        start = min_elem_index + 1
        for i in range(start, len(arr)):
            if arr[i] < min_elem:
                min_elem = arr[i]
                found_min_elem_index = i

        if found_min_elem_index:
            arr[found_min_elem_index], arr[min_elem_index] = arr[min_elem_index], arr[found_min_elem_index]

        min_elem_index += 1
    return arr





input_array = [3, 44, 38, 5, 47, 37, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(f'input array={input_array}')
print(selection_sort(input_array))