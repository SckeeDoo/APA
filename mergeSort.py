import random
import time

def mergeSort(A):
    if len(A)>1:
        mid = len(A)//2
        leftHalf = A[:mid]
        rightHalf = A[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0
        j=0
        k=0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                A[k]=leftHalf[i]
                i=i+1
            else:
                A[k]=rightHalf[j]
                j=j+1
            k=k+1

        while i < len(leftHalf):
            A[k]=leftHalf[i]
            i=i+1
            k=k+1

        while j < len(rightHalf):
            A[k]=rightHalf[j]
            j=j+1
            k=k+1

def quickSort(A):
   quickSortHelper(A,0,len(A)-1)

def quickSortHelper(A,first,last):
   if first<last:

       splitpoint = partition(A,first,last)

       quickSortHelper(A,first,splitpoint-1)
       quickSortHelper(A,splitpoint+1,last)


def partition(A,first,last):
   pivotvalue = A[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and A[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while A[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = A[leftmark]
           A[leftmark] = A[rightmark]
           A[rightmark] = temp

   temp = A[first]
   A[first] = A[rightmark]
   A[rightmark] = temp

   return rightmark

A = []
for i in range():
    A.append(i)
#random.shuffle(A)

start = time.time()
quickSort(A)
end = time.time()

print "Quick sort time execution : ",end - start


A = []
B = []
for i in range(900):
    A.append(i)
#random.shuffle(A)

start = time.time()
mergeSort(A)
end = time.time()
print "Merge sort time execution : ", end - start

