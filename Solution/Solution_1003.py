T = int(input())

for i in range (0,T):
  N = int(input())

  memo0Count=[0 for i in range(41)]
  memo0Count[0]=1
  memo0Count[1]=0
  
  memo1Count=[0 for i in range(41)]
  memo1Count[0]=0
  memo1Count[1]=1

  for i in range(2,41):
    memo0Count[i]=memo0Count[i-2]+memo0Count[i-1]
    memo1Count[i]=memo1Count[i-2]+memo1Count[i-1]

  print(memo0Count[N],memo1Count[N])
