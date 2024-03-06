def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг, указывающий на то, были ли сделаны обмены на текущей итерации
        swapped = False
        for j in range(0, n-i-1):
            # Сравниваем элементы попарно
            if arr[j] > arr[j+1]:
                # Если текущий элемент больше следующего, меняем их местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если на текущей итерации не было сделано ни одного обмена, массив уже отсортирован
        if not swapped:
            break
    return arr

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print("Отсортированный массив:", sorted_array)