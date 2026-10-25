def bubble_sort(list1):
    list_clone = list1.copy()
    list_len = len(list_clone)
    count = 0
    rear = 0
    for i in range(list_len - 1):
        for j in range(list_len-1-i):
            count += 1
            if list_clone[j] > list_clone[j+1]:
                list_clone[j], list_clone[j+1] = list_clone[j+1], list_clone[j]
                rear += 1
    print(f"for list of length {list_len} there are {count} checks and {rear} rearrangement")
    return list_clone
                