def binary_search(arr,target):
  low,high = 0,len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] <target:
      low = mid + 1
    else:
      high = mid + 1
    return - 1
arr =[ 2, 5, 8, 12 , 16, 23, 38, 56, 72, 91]
target = int(input("Enter a number to search : "))
result = binary_search(arr , target)
if result !=-1:
  print("Number found at index ", result)
else:
  print("Number not found in the array")
     