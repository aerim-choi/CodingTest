N= int(input())
A=list(map(int,input().split()))

M=int(input())
B=list(map(int,input().split()))

#A를 정렬
A.sort()
#[1,2,3,4,5]
def binarySearch(A,num,low,high):
  if high < low :
    return 0
  mid = ((low+high) // 2) #5/2=2
  if num < A[mid] :
    return binarySearch(A,num,low,mid-1)
  elif num > A[mid] :
    return binarySearch(A,num,mid+1,len(A)-1)
  else: 
    return 1

for i in range(0,M):
  print(binarySearch(A,B[i],0,len(A)-1))
