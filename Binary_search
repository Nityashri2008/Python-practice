arr = [10, 20, 30, 40, 50]
target = 40

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print("Found at index:", mid)
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Not found")
