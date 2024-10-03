def sum_even_index_multiply_last(arr):
    if not arr:
        return 0
    sum_even = sum(arr[i] for i in range(0, len(arr), 2))
    return sum_even * arr[-1]

arr = [0, 1, 7, 2, 4, 8]
result = sum_even_index_multiply_last(arr)
print(result)