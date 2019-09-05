def upAdjust(array):
    childIndex = len(array) -1
    parentIndex = (childIndex -1)//2
    temp = array[childIndex]
    while childIndex > 0 and temp < array[parentIndex]:
        array[childIndex] = array[parentIndex]
        childIndex = parentIndex
        parentIndex = (parentIndex - 1)//2
    array[childIndex] = temp

def downAdjust(array, parentIndex, length):
    temp = array[parentIndex]
    childIndex = 2 * parentIndex +1
    while childIndex < length:
        if childIndex +1 <length and array[childIndex+1] < array[childIndex]:
            childIndex +=1
        if temp < array[childIndex]:
            break
        array[parentIndex] = array[childIndex] 
        parentIndex = childIndex
        childIndex = 2 * parentIndex +1
    
    array[parentIndex] = temp


def buildHeap(array):
    for i in range((len(array)-2)//2, -1,-1):
        downAdjust(array,i,len(array))


if __name__=="__main__":
    array = [1,3,2,6,5,7,8,9,10,0]
    upAdjust(array)
    print(array)
    array = [7,1,3,10,5,2,8,9,6]
    buildHeap(array)
    print(array)




