# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    print(f"Before:{arr}")
    count = 0
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                print(f"arr[{j}]")
                count+=1
                print(f"if arr[j] ({arr[j]}) < arr[smallest_index] ({arr[smallest_index]}) ")
                smallest_index = j
                print(f"Smallest_index = {smallest_index}")
                print(f"After:(Run#{count}{arr}")
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        print(f"End:{arr}")
    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(arr1)  # *  =>  [0,1,2,3,4,5,6,7,8,9]


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                print(f"arr[{arr[j]}] > arr[{arr[j+1]}]")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr


arr1 = [5,4,3,2,1]
print(bubble_sort(arr1))

# arr1 = ['b','d','f','a','c','e']


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
