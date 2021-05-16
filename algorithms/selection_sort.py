def find_min(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def select_sort(array):
    sorted_list = []
    for i in range(len(array)):
        smallest = find_min(array)
        sorted_list.append(array.pop(smallest))
    return sorted_list


mass = [6, 3, 76, 44, 98, 4, 1]
print(select_sort(mass))

