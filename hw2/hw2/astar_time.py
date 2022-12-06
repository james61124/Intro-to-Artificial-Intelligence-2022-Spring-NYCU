import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar_time(start, end):
    # Begin your code (Part 6)
    #raise NotImplementedError("To be implemented")
    ad_list={}
    with open('edges.csv', newline='') as edgeFile:
        rows = csv.DictReader(edgeFile)
        for row in rows:
            key = int(row['start'])
            value = [int(row['end']), float(row['distance']), float(row['speed limit'])]
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
    time=0
    ucs_visited=0
    ucs=[]
    visited=[]
    visited.append(start)
    ucs_visited=ucs_visited+1
    path={}
    for vertex in ad_list[start]:
        temp=[vertex[1]/vertex[2]*3.6+heuristic[start]/60*3.6,vertex[1]/vertex[2]*3.6,start,vertex[0]]
        ucs.append(temp)
    while ucs:
        min_vertex = min(ucs)
        #time=time+min_vertex[1]
        if min_vertex[3] in visited:
            ucs.remove(min_vertex)
            continue
        if min_vertex[3] in ad_list:
            visited.append(min_vertex[3])
            ucs_visited=ucs_visited+1
            tmp=[min_vertex[2],min_vertex[1]]
            path[min_vertex[3]]=tmp
            #print(min_vertex[3],min_vertex[2])
            for vertex in ad_list[min_vertex[3]]:
                if vertex[0] not in visited:
                    temp=[vertex[1]/vertex[2]*3.6+min_vertex[1]+heuristic[vertex[0]]/60*3.6,vertex[1]/vertex[2]*3.6+min_vertex[1],min_vertex[3],vertex[0]]
                    ucs.append(temp)
        if min_vertex[3]==end:
            time=min_vertex[1]
            break
        ucs.remove(min_vertex)
    #time=0
    ucs_path=[]
    des=end
    while des!=start:
        ucs_path.insert(0,des)
        #bfs_dist=bfs_dist+path[des][1]
        #time=time+path[des][1]
        
        des=path[des][0]
    ucs_path.insert(0,des)
    return ucs_path, time, ucs_visited
    # End your code (Part 6)


if __name__ == '__main__':
    path, time, num_visited = astar_time(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
