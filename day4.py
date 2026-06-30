n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
left = 0
right = n - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(*arr)