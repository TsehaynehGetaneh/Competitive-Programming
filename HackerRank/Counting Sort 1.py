def countingSort(arr):
    result_arr = [0] * 100
    for i in range(len(arr)):
        result_arr[arr[i]] +=1
    return result_arr