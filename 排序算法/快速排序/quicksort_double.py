import random
import time

def quicksort(arr, startIndex, endIndex):
    if startIndex >= endIndex:
        return
    pivotIndex = partition(arr, startIndex, endIndex)
    quicksort(arr, startIndex, pivotIndex-1)
    quicksort(arr,pivotIndex+1,endIndex)


def partition(arr, startIndex,endIndex):
    pivotIndex = random.randrange(0,endIndex)
    switch(arr, pivotIndex, startIndex)
    pivot=arr[startIndex]
    left = startIndex
    right = endIndex
    while left != right:
        while left<right and arr[right] > pivot:
            right -=1
        while left < right and arr[left] <= pivot:
            left +=1
        if left<right:
            switch(arr, left, right)
    switch(arr, startIndex, left)
    return left


def switch(arr, indexLeft, indexRight):
    arr[indexLeft],arr[indexRight] = arr[indexRight], arr[indexLeft]


if __name__=="__main__":
    arr = [4,4,6,5,3,2,8,1]
    start = time.time()
    quicksort(arr, 0, len(arr)-1)
    end = time.time()
    print("result: ", arr)
    print("快速排序 双边循环法 耗时： {}".format(end-start))
