n = int(input())
songs = list(map(int,input().split()))
max_cnt = 1
max_no = songs[0]
for i in songs:
    if max_cnt <= songs.count(i):
        max_cnt =songs.count(i) 
        max_no = i

print(max_no)
