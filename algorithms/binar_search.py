def bisearch(massive, item):
    start = 0
    finish = len(massive) - 1

    while start <= finish:
        middle = (start + finish) // 2
        element = massive[middle]
        
        if element == item:
            return middle
        elif element > item:
            finish = middle - 1
        else:
            start = middle + 1


our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
item = 9
print(bisearch(our_list, item))
