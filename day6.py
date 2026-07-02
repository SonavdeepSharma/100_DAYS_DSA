n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the sorted array elements: ").split()))

if n == 0:
    print("Array is empty.")
else:
    unique_index = 0

    for current_index in range(1, n):
        if arr[current_index] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[current_index]

    print("Unique elements are:", end=" ")
    for i in range(unique_index + 1):
        print(arr[i], end=" ")