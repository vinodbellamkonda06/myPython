def bubblesort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [22, 3, 1, 6, 3, 65, 7, 4]
bubblesort(arr)
arr_sort = []
for i in range(len(arr)):
    arr_sort.append(arr[i])
print(arr_sort)


def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")

list_of_elements = [4, 2, 8, 9, 3, 7]

x = int(input("Enter number to search: "))

found = False

for i in range(len(list_of_elements)):
    if list_of_elements[i] == x:
        found = True
        print("%d found at %dth position" % (x, i))
        break

if found is False:
    print("%d is not in list" % x)

