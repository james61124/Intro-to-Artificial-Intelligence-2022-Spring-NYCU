import csv
edgeFile = 'edges.csv'


def dfs(start, end):
    # Begin your code (Part 2)
    """
    Use stack to implement dfs.
    Like bfs, pop the first element in the stack.
    Diferent from bfs is that we insert the children of the element to the front of the stack.
    I use the dictionary "path" to record the father of the child as well. 
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
    
    stack=[]
    visited=[]
    path={}
    t=[start,start,0]
    #stack = t + stack
    stack.insert(0,t)
    bfs_visited=0
    while stack:
        vertex = stack[0]
        del stack[0]
        if vertex[1] in visited:
            continue
        visited.append(vertex[1])
        bfs_visited=bfs_visited+1
        if vertex[1]!=start and vertex[1] in ad_list:
            tmp=[vertex[0],vertex[2]]
            path[vertex[1]]=tmp
        if vertex[1]==end:
            break
        if vertex[1] in ad_list:
            substack=[]
            for neighbor in ad_list[vertex[1]]:
                temp=[vertex[1],neighbor[0],neighbor[1]]
                substack.insert(0,temp)
            stack = substack + stack          
    ans=[]
    des=end
    bfs_dist=0.0
    while des!=start:
        ans.insert(0,des)
        bfs_dist=bfs_dist+path[des][1]
        des=path[des][0]
    ans.insert(0,des)
    bfs_path=ans

    return bfs_path, bfs_dist, bfs_visited
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
