## 使用最大堆进行排序
def downAdjust(array, parentIndex, length):
    temp = array[parentIndex]
    childIndex = 2 * parentIndex +1
    while childIndex < length:
        if childIndex +1 <length and array[childIndex] < array[childIndex +1]:
            childIndex +=1
        if temp > array[childIndex]:
            break
        array[parentIndex] = array[childIndex] 
        parentIndex = childIndex
        childIndex = 2 * parentIndex +1
    array[parentIndex] = temp

def buildHeap(array):
    for i in range((len(array)-2)//2, -1,-1):
        downAdjust(array,i,len(array))

def heapSort(array):
    # 从最后一个有子节点的孩子还是调整最大堆
    buildHeap(array)
    print(array)
    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    length = len(array)
    for end in range(len(array) -1, 0, -1):
        array[0], array[end] = array[end], array[0]
        length -=1
        downAdjust(array, 0, length)
        print(array)

if __name__ == "__main__":
    array= [1,3,2,6,7,8,9,11,4]
    heapSort(array)
    
