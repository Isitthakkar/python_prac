K=int(input())
Room_list=list(map(int,input().split()))
a=len(Room_list)
Room_list.sort()
count=0
i=0
while(i<a):
    count=Room_list.count(Room_list[i])
    if(count==K):
        i=i+K
    else:
        print(Room_list[i])
        break