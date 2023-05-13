def dfs(graph, v, visited):
    #현재 노드 방문 처리 
    visited[v] = True
    print(v,end =" ")
    # 연결된 노드를 재귀적으로 방문
    for i in graph[v]: # ex) 1번 노드 [2,3,8] => 2번 노드 
        if not visited[i]: # not False => True # 노드가 방문 안한 노드여야
            dfs(graph, i, visited)

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

visited = [False] * 9 

dfs(graph, 1, visited)