# You are provided with the heights of 11 cricket players (in centimeters). Your task is to identify the tallest player, who will be selected as the captain of the team.


lis=list(map(int,input().split()))
max=lis[0]
for i in lis:
	if(max < i):
		max=i
print(max)
