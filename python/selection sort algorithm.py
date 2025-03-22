def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
print("Sorted array:", selection_sort(arr))
