def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0

    while low <= high:

        mid = (high + low) // 2

        # підрахунок кількість операцій
        count += 1

        if arr[mid] < x:
            low = mid + 1

            if arr[low] > x:
                return count, arr[low]

        elif arr[mid] > x:
            high = mid - 1

            if arr[high] < x:
                return count, arr[mid]
            elif high == 0 and arr[high] > x:
                return count, arr[high]

    return -1


arr = [2.5, 3.7, 4.8, 11.1, 13.1, 13.2, 30.5, 40.7, 56.7, 67.3]
# arr = [int(round(x, 0)) for x in arr]

x = 10

result = binary_search(arr, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
