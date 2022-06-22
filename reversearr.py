def reversearr(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1

def leftrotate(arr,d):
        n = len(arr)
        reversearr(arr, 0, d-1)
        reversearr(arr, d, n-1)
        reversearr(arr, 0, n-1)

def printarr(arr):
            for i in range(0, len(arr)):
                print (arr[i])

                arr = [1, 2, 3, 4, 5, 6, 7]
                leftrotate(arr,2)
                printarr(arr)