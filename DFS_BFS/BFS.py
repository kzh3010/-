from collections import deque 

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v= queue.popleft()
        print(v,end="")
        for i in graph[v]:
            if not visited[i]:
                #방문하지 않은 노드 큐에 삽입
                queue.append(i)
                # 방문처리
                visited[i] = True

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

vistied = [False] * 9 
bfs(graph, 1, vistied)
    