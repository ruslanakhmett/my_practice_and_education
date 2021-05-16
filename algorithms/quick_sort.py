def quick_sort(array):
    if len(array) < 2:
        return array
    point = array[0]
    low = [i for i in array[1:] if i <= point]
    high = [i for i in array[1:] if i > point]
    return quick_sort(low) + [point] + quick_sort(high)


print(quick_sort([7, 4, 2, 9, 6]))