import csv
edgeFile = 'edges.csv'


def ucs(start, end):
    # Begin your code (Part 3)
    """
    ucs is a list. The element in it is a list contains [distance from start to this node, father, the node].
    Using "ucs", we pop the minimum distance in "ucs". 
    If the node haven't been visited, we add its children who have not been visited as weel to "ucs".
    Repeat the process until "end" is visited.
    """
    #raise NotImplementedError("To be implemented")
    ad_list={}
    with open('edges.csv', newline='') as edgeFile:
        rows = csv.DictReader(edgeFile)
        for row in rows:
            key = int(row['start'])
            value = [int(row['end']), float(row['distance'])]
            if key not in ad_list.keys():
                ad_list[key] = list()
            ad_list[key].append(value)
    
    ucs_dist=0
    ucs_visited=0
    ucs=[]
    visited=[]
    visited.append(start)
    ucs_visited=ucs_visited+1
    path={}
    for vertex in ad_list[start]:
        temp=[vertex[1],start,vertex[0]]
        ucs.append(temp)
    while ucs:
        min_vertex = min(ucs)
        if min_vertex[2] in visited:
            ucs.remove(min_vertex)
            continue
        if min_vertex[2] in ad_list:
            visited.append(min_vertex[2])
            ucs_visited=ucs_visited+1
            path[min_vertex[2]]=min_vertex[1]
            for vertex in ad_list[min_vertex[2]]:
                if vertex[0] not in visited:
                    temp=[vertex[1]+min_vertex[0],min_vertex[2],vertex[0]]
                    ucs.append(temp)
        if min_vertex[2]==end:
            ucs_dist=min_vertex[0]
            break
        ucs.remove(min_vertex)
    ucs_path=[]
    des=end
    while des!=start:
        ucs_path.insert(0,des)
        des=path[des]
    ucs_path.insert(0,des)
    return ucs_path, ucs_dist, ucs_visited
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
