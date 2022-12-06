import csv
edgeFile = 'edges.csv'


def bfs(start, end):
    # Begin your code (Part 1)
    """
    First, convert "edges.csv" to adjency list. This part appears in four algorithms.
    Second, do bsf.
    I implement bfs by queue. Pop the first element in queue and see if the element was visited.
    If the element is visited, then pop the first element again. Repeat the process.
    If the element isn't visited, then add the children of the element to the last of the queue.
    If the element is end itself, it means that we have found the route. As a result, we can break the loop.
    The dictionary "path" records Father of the element. Key is child, and value is father.
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
    
    visited = [] # List for visited nodes.
    queue = []     #Initialize a queue
    visited.append(start)
    queue.append(start)
    path={}
    bfs_visited=0
    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        if m==end:
            break
        if m in ad_list:
            for neighbour in ad_list[m]:
                if neighbour[0] not in visited:
                    bfs_visited=bfs_visited+1
                    visited.append(neighbour[0])
                    queue.append(neighbour[0])
                    temp=[]
                    temp.append(m)
                    temp.append(neighbour[1])
                    path[neighbour[0]]=temp
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
    #raise NotImplementedError("To be implemented")
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
