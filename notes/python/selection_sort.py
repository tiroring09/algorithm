def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i

        # 최소값 탐색
        for j in range(min_idx + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr