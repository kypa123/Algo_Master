import sys
from pprint import pprint
input = sys.stdin.readline
arr=[]
dx=[0,1,1,-1]
dy= [1,0,1,1]
for i in range(19):
    arr.append(list(map(int, input().split())))
for i in range(19):
    for j in range(19):
        if arr[i][j]!=0:
            att = arr[i][j]
            for k in range(4):
                cnt=1
                nx= i+dx[k]
                ny = j+dy[k]
                while 0<=nx<19 and 0<=ny<19 and arr[nx][ny]==att:
                    cnt+=1
                    if cnt==5:
                        if 0<=i-dx[k]<19 and 0<=j-dy[k]<19 and arr[i-dx[k]][j-dy[k]]==att:
                            break
                        if 0<=nx+dx[k]<19 and 0<=ny+dy[k]<19 and arr[nx+dx[k]][ny+dy[k]]==att:
                            break
                        sys.exit()
                    nx+=dx[k]
                    ny+=dy[k]
print(0)
