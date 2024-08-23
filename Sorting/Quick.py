def swap(mylist,index1,index2):
    mylist[index1],mylist[index2]=mylist[index2],mylist[index1]

def pivot(mylist,pivot_index,end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1,end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist,swap_index,i)
    swap(mylist,pivot_index,swap_index)
    return swap_index

def _quick_sort(mylist,left,right):
    if left < right:
        pivot_index = pivot(mylist,left,right)
        _quick_sort(mylist,left,pivot_index-1)
        _quick_sort(mylist,pivot_index+1,right)
    return mylist

def quick_sort(mylist):
    return _quick_sort(mylist,0,len(mylist)-1)

mylist=[4,6,1,7,3,2,5]
print("Unsorted array :",mylist)
print("Sorted array :",quick_sort(mylist))  
