totaldist = 0.0
visited = []
parent = {}
dist = {}
queue = []
queue.append(start)
while queue:
    top = queue.pop(0) #取出最前面的
    if top == end:
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
            totaldist += dist[path[-1]]
        path.reverse()
        return path, totaldist, len(visited)
    if top not in visited:
        visited.append(top)
        with open(edgeFile, newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                if row[0].isdigit():
                    row[0] = int(row[0])
                    row[1] = int(row[1])
                    row[2] = float(row[2])
                    if ( row[0] == top):
                        print(row[1])
                        parent[ row[1] ] = top
                        dist[ row[1] ] = row[2]
                        queue.append( row[1] )