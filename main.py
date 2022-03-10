from collections import deque

def output(path):
    with open("output", "w") as file:
        length = str(len(path))
        path = [str(node) for node in path]
        path = " ".join(path)
        file.write(length + "\n" + path)


def input_graph():
    first = True

    with open("input") as file:
        graph = []
        for line in file:
            if (first):
                nodes, edges = line.split()
                nodes, edges = int(nodes), int(edges)
                first = False
            else:
                line = line.strip()
                line = line.split()
                line = [int(val) for val in line]
                graph.append(line)
        return nodes, graph

def make_graph(data, length):
    graph = [False for _ in range(length)]
    for x, y, edge in data:
        if not(graph[x]):
            graph[x] = {x: 1}

        if not(graph[y]):
            graph[y] = {y: 1}

        graph[x].update({y: edge})
        graph[y].update({x: edge})
    return graph

def DFS(graph, length):
    queue = deque()
    visited = [False for _ in range(length)]
    visited[0] = [1, 0]
    queue.append([0, 0])
    while(queue):
        node, ancestor = queue.pop()
        visited[node] = [graph[node][ancestor] * visited[ancestor][0], ancestor]
        for neighbour in graph[node]:
            if not(visited[neighbour]):
                queue.append([neighbour, node])
            else:
                if (visited[neighbour][0]*graph[neighbour][node]*visited[node][0]==-1):
                    path1 = []
                    actual = neighbour
                    while(True):
                        path1.append(actual)
                        actual = visited[actual][1]
                        if (actual==0):
                            break
                    path1.append(0)
                    path2 = []
                    actual = node
                    while (True):
                        path2.append(actual)
                        actual = visited[actual][1]
                        if (actual == 0):
                            break
                    return path1, path2

nodes, inp = input_graph()
graph = make_graph(inp, nodes)
path1, path2 = DFS(graph, nodes)
final_path = path1 + path2[::-1] + [path1[0]]
output(final_path)