import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar(start, end):
    # Begin your code (Part 4)
    """
    Similar to ucs. We use "ucs" to record the elements.
    Different from ucs.py, elements in "ucs" is [distance from start + heuristic, distance from start, father, node]
    We are looking for the minimum "distance from start + heuristic" and repeat the process.
    """
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
        des=path[des]
    ucs_path.insert(0,des)
    return ucs_path, ucs_dist, ucs_visited
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
