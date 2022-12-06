import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'



start = 2270143902
end = 1079387396
ad_list={}
with open('edges.csv', newline='') as edgeFile:
    rows = csv.DictReader(edgeFile)
    for row in rows:
        key = int(row['start'])
        value = [int(row['end']), float(row['distance'])]
        if key not in ad_list.keys():
            ad_list[key] = list()
        ad_list[key].append(value)

heuristic={}
with open('heuristic.csv', newline='') as heuristicFile:
    rows = csv.DictReader(heuristicFile)
    for row in rows:
        key = int(row['node'])
        value = float(row[str(end)])
        # if key not in heuristic.keys():
        #     heuristic[key] = list()
        #heuristic[key].append(value)
        heuristic[key]=value

ucs_dist=0
ucs_visited=0
ucs=[]
visited=[]
visited.append(start)
ucs_visited=ucs_visited+1
path={}
for vertex in ad_list[start]:
    temp=[vertex[1]+heuristic[start],vertex[1],start,vertex[0]]
    ucs.append(temp)
while ucs:
    min_vertex = min(ucs)
    if min_vertex[3] in visited:
        ucs.remove(min_vertex)
        continue
    if min_vertex[3] in ad_list:
        visited.append(min_vertex[3])
        ucs_visited=ucs_visited+1
        path[min_vertex[3]]=min_vertex[2]
        #print(min_vertex[3],min_vertex[2])
        for vertex in ad_list[min_vertex[3]]:
            if vertex[0] not in visited:
                temp=[vertex[1]+min_vertex[1]+heuristic[vertex[0]],vertex[1]+min_vertex[1],min_vertex[3],vertex[0]]
                ucs.append(temp)
    if min_vertex[3]==end:
        ucs_dist=min_vertex[1]
        break
    ucs.remove(min_vertex)

ucs_path=[]
des=end
while des!=start:
    ucs_path.insert(0,des)
    #bfs_dist=bfs_dist+path[des][1]
    des=path[des]
ucs_path.insert(0,des)
#print(ucs_path)