def quick_sort(array, start, end):
    pivot = start
    right = end
    left = pivot + 1
    if start >= end:
        return
    while left <= right: # left가  right보다 크면 stop ( 엇갈리면 )
        while (left <= end and array[left] <= array[pivot]): # 큰 것 찾을 때 까지
            left += 1
        while (right > start and array[right] > array[pivot]): # 작은 것 찾을 때 까지
            right -= 1
        if left > right : # 엇갈리면 pivot이랑 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array,start, right-1) # 왼쪽 행렬
    quick_sort(array,left, end) # 오른쪽 행렬
start = 0
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, start, len(array)-1)
print(array)

# using slicing
def quick_sort(array):
    if (len(array) <= 1):
        return array
    pivot = array[0]
    tail = array[1:]

    left_array = [left for left in tail if left <= pivot]
    right_array = [right for right in tail[::-1] if right > pivot]

    return quick_sort(left_array)+[pivot]+quick_sort(right_array)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))


