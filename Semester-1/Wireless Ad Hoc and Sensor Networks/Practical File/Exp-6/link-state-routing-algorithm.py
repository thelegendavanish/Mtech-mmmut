# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Implementation of Link State Routing Algorithm
# Description:
#   This program simulates the Link State Routing (LSR) algorithm.
#   Each node calculates the shortest path to all other nodes using 
#   Dijkstra’s algorithm. The input is taken as a cost adjacency matrix.
# ------------------------------------------------------------------------------

import heapq

def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [float('inf')] * n
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        (dist, u) = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                new_dist = dist + graph[u][v]
                if new_dist < distance[v]:
                    distance[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    return distance


def link_state_routing():
    print("\n=== Link State Routing Algorithm Simulation ===\n")
    n = int(input("Enter number of nodes: "))

    print("Enter cost adjacency matrix (0 for no direct link):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        graph.append(row)

    print("\nShortest Path from each node to every other node:\n")
    for i in range(n):
        dist = dijkstra(graph, i)
        print(f"From Node {i+1}: ", end="")
        for j in range(n):
            if dist[j] == float('inf'):
                print("∞", end=" ")
            else:
                print(dist[j], end=" ")
        print()


if __name__ == "__main__":
    link_state_routing()



