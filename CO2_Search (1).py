from collections import deque
import heapq

graph = {
    'S': [('A',1), ('B',2)],
    'A': [('C',2)],
    'B': [('D',1)],
    'C': [('G',3)],
    'D': [('G',2)],
    'G': []
}

heuristic = {
    'S':5,
    'A':4,
    'B':2,
    'C':2,
    'D':1,
    'G':0
}

def bfs(start):
    q = deque([start])
    visited = set()

    while q:
        node = q.popleft()
        print(node,end=" ")
        visited.add(node)

        for neighbor,_ in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)

def dfs(start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        print(node,end=" ")
        visited.add(node)

        for neighbor,_ in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

def ucs(start, goal):
    pq = [(0,start)]

    while pq:
        cost,node = heapq.heappop(pq)

        if node == goal:
            return cost

        for neighbor,w in graph[node]:
            heapq.heappush(pq,(cost+w,neighbor))

def astar(start, goal):
    pq = [(heuristic[start],0,start)]

    while pq:
        f,g,node = heapq.heappop(pq)

        if node == goal:
            return g

        for neighbor,w in graph[node]:
            heapq.heappush(
                pq,
                (g+w+heuristic[neighbor],g+w,neighbor)
            )