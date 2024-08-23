# def Insertion_Sort(arr):
#     for i in range(1,len(arr)):
#         for j in range(i):
#             if arr[i] < arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#     return arr

def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            arr[j]=temp
            j=j-1
    return arr
arr=[3,1,4,2,5]
print(Insertion_Sort(arr))