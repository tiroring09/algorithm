def bubble(nums):
    size = len(nums)
    while size > 1:
        for i in range(size - 1):   # 인덱스가 전체인덱스보다 1작아야 함/ 아니면 인덱스가 1부터시작해서 끝까지 가는데 i-1과 i를 비교해도 된다.
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        size -= 1
    return nums

def bubble2(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

asdf = [5, 4, 2, 6, 2]
print(bubble(asdf))