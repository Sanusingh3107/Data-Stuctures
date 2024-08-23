def bubble_sort(n):
    for i in range(len(n)-1,0,-1):
        for j in range(i):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n
n=list(map(int,input("Enter array : ").split()))
print("Unsorted Arraye is",n)
print("Sorted Array is",bubble_sort(n))