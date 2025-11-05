# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Simulation of Distance Vector Routing Algorithm
# Description:
#   This program simulates the Distance Vector Routing algorithm used in
#   computer networks. Each node updates its routing table based on the
#   distance vectors received from its neighbors until all tables converge.
# ------------------------------------------------------------------------------

# Function to implement Distance Vector Routing
def distance_vector_routing(n, cost):
    distance = [row[:] for row in cost]  # Copy cost matrix
    next_hop = [[j if cost[i][j] != 999 else -1 for j in range(n)] for i in range(n)]

    print("\nInitial Distance Tables:")
    for i in range(n):
        print(f"Router {i+1}: {distance[i]}")

    iteration = 0
    while True:
        iteration += 1
        updated = False

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if distance[i][j] > cost[i][k] + distance[k][j]:
                        distance[i][j] = cost[i][k] + distance[k][j]
                        next_hop[i][j] = k
                        updated = True

        if not updated:
            break

    print("\n--- Final Distance Tables after Convergence ---")
    for i in range(n):
        print(f"\nRouter {i+1}:")
        print("Destination\tCost\tNext Hop")
        for j in range(n):
            if i == j:
                continue
            nh = f"Router {next_hop[i][j]+1}" if next_hop[i][j] != -1 else "-"
            print(f"   {j+1}\t\t {distance[i][j]}\t  {nh}")


# Main simulation
def simulate_dvr():
    print("\n--- Distance Vector Routing Simulation ---")
    n = int(input("Enter the number of routers: "))

    print("\nEnter the cost matrix (use 999 for infinity):")
    cost = []
    for i in range(n):
        row = list(map(int, input(f"Cost from router {i+1} to others: ").split()))
        cost.append(row)

    distance_vector_routing(n, cost)


# Run simulation
simulate_dvr()



