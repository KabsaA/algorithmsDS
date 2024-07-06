def binary_search(arr,targ):
  low = 0
  high = len(arr)-1

  while low < high:
    mid = (low + high) // 2

    if arr[mid] == targ:
      return mid
    
    elif arr[mid] < targ:
      low = mid + 1

    elif arr[mid] > targ:
      high = mid - 1
    
  else:
    return -1
