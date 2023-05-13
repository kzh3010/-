import sys

input = sys.stdin.readline

node = int(input())
number = int(input())
net = [[] for _ in range(node + 1)]

for i in range(number):
    a = list(map(int,input().split()))
    x, y = a[0], a[1]
    net[x].append(y)
    net[y].append(x)

def DFS(graph, v, visited):
    visited[v] = True 
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

visited = [False] * (node + 1)

DFS(net, 1, visited)
ans = (visited.count(True) - 1)
print(ans)
