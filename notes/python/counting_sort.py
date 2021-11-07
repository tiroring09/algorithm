def counting(arr):
    # arr의 최대값까지 포함되도록 counter인덱스를 생성한다. 갯수가 1개 많아야 maxval의 인덱스 값까지 생성한다.
    maxval = max(arr)
    counter = [0] * (maxval + 1)
    result = [0] * len(arr) # 정렬된 배열이 될 예정

    # 딕셔너리 counting하는 것 처럼 갯수를 세어준다.
    for val in arr:
        counter[val] += 1

    # 처음부터 자기자신까지의 갯수를 저장한다.
    for i in range(1, len(counter)):    # counter배열의 index 1부터 끝까지 호출
        counter[i] = counter[i] + counter[i - 1]

    for val in arr:
        counter[val] -= 1   # val의 갯수에서 1을 뺀 값을
        index = counter[val]    # 인덱스로삼아
        result[index] = val # 그 위치에 val이 들어간다

    return result

a = [1, 5, 7, 3, 9, 10, 4, 5, 6, 6, 6]
print(counting(a))