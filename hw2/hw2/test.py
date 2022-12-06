import csv
edgeFile = 'edges.csv'
csvfile = open(edgeFile)
start, end = 1, 6
r = csv.reader(csvfile)     # 讀取 csv 檔案
ad_list={1:[[2,9],[3,4]],2:[[1,9],[3,2],[4,7]],3:[[1,4],[2,2],[4,1],[5,6]],4:[[2,7],[5,4],[6,8]],5:[[2,3],[4,4],[6,2]],6:[[4,8],[5,2]]}
# with open('edges.csv', newline='') as edgeFile:
#     rows = csv.DictReader(edgeFile)
#     for row in rows:
#         key = int(row['start'])
#         value = [int(row['end']), float(row['distance'])]
#         if key not in ad_list.keys():
#             ad_list[key] = list()
#         ad_list[key].append(value)

ucs=[]
visited=[]
visited.append(start)
path={}
for vertex in ad_list[start]:
    temp=[vertex[1],start,vertex[0]]
    ucs.append(temp)
print(ucs)
while ucs:
    min_vertex = min(ucs)
    if min_vertex[2] in visited:
        ucs.remove(min_vertex)
        continue
    print(min_vertex)
    if min_vertex[2] in ad_list:
        visited.append(min_vertex[2])
        path[min_vertex[2]]=min_vertex[1]
        for vertex in ad_list[min_vertex[2]]:
            if vertex[0] not in visited:
                temp=[vertex[1]+min_vertex[0],min_vertex[2],vertex[0]]
                ucs.append(temp)
    ucs.remove(min_vertex)
                

ucs_dist=0
ucs_visited=0
ucs_path=[]
des=end
while des!=start:
    ucs_path.insert(0,des)
    #bfs_dist=bfs_dist+path[des][1]
    des=path[des]
ucs_path.insert(0,des)
print(ucs_path)
