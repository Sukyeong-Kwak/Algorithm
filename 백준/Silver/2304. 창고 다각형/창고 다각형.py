n = int(input())
columns = [list(map(int, input().split())) for _ in range(n)]
columns.sort(key=lambda x:x[0])

# print(columns)

max_height = 0
max_location = []
for i in range(len(columns)):
    if columns[i][1] > max_height:
        max_height = columns[i][1]
        max_location = [i]
    elif columns[i][1] == max_height:
        max_location.append(i)
    # print(max_location)

# print(max_location)

area = 0
height = 0

for i in range(max_location[0]):
    height = max(columns[i][1], height)
    area += (columns[i+1][0] - columns[i][0])*height
    # print(area)
    
height = 0

for i in range(len(columns)-1, max_location[-1], -1):
    height = max(columns[i][1], height)
    area += (columns[i][0] - columns[i-1][0])*height
    # print(area)
    
if len(max_location) == 1:
    area += max_height
else:
    area += max_height *(columns[max_location[-1]][0] - columns[max_location[0]][0]+1)


print(area)