import csv
edgeFile = 'edges.csv'


def recursive(visited, ad_list, node, end, path, isfinish, bfs_visited):  #function for dfs 
    if node not in visited:
        #print(node)
        if node==end:
            return path, bfs_visited, 1
        visited.append(node)
        bfs_visited=bfs_visited+1
        if node in ad_list:
            for neighbour in ad_list[node]:
                # temp=[]
                # temp.append(node)
                # temp.append(neighbour[1])
                #path[neighbour[0]]=temp
                path.append(node)
                path, bfs_visited, isfinish = recursive(visited, ad_list, neighbour[0], end, path, isfinish, bfs_visited)
                #print(isfinish)
                if isfinish==1:
                    return path, bfs_visited, 1
            return path, bfs_visited, isfinish
        else:
            return path, bfs_visited, isfinish
    else:
        return path, bfs_visited, isfinish


def dfs(start, end):
    # Begin your code (Part 2)
    #raise NotImplementedError("To be implemented")
    ad_list={}
    visited=[]
    path=[]
    with open('edges.csv', newline='') as edgeFile:
        rows = csv.DictReader(edgeFile)
        for row in rows:
            key = int(row['start'])
            value = [int(row['end']), float(row['distance'])]
            if key not in ad_list.keys():
                ad_list[key] = list()
            ad_list[key].append(value)
    path, bfs_visited, temp = recursive(visited, ad_list, start, end, path, 0, 0)
    print(path)
    dfs_path=[]
    des=end
    bfs_dist=0.0
    # while des!=start:
    #     print(des)
    #     dfs_path.insert(0,des)
    #     bfs_dist=bfs_dist+path[des][1]
    #     des=path[des][0]
    # dfs_path.insert(0,des)
    return path, bfs_dist, bfs_visited




    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
