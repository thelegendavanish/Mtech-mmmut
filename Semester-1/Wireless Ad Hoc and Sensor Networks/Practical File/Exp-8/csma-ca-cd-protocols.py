# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Performance Analysis of CSMA/CD and CSMA/CA Protocols
# Description:
#   This program simulates the working of CSMA/CD (Collision Detection)
#   and CSMA/CA (Collision Avoidance) protocols.
#   It compares their performance based on the number of collisions and
#   successful transmissions during data transfer attempts.
# ------------------------------------------------------------------------------

import random
import time

def csma_cd_simulation(stations, attempts):
    print("\n=== CSMA/CD (Collision Detection) Simulation ===")
    collision_count = 0
    success_count = 0

    for i in range(attempts):
        transmitting = [s for s in range(stations) if random.random() < 0.4]
        if len(transmitting) > 1:
            collision_count += 1
            print(f"Attempt {i+1}: Collision between stations {transmitting}")
            # Backoff before retransmission
            time.sleep(0.1 * random.random())
        elif len(transmitting) == 1:
            success_count += 1
            print(f"Attempt {i+1}: Station {transmitting[0]} transmitted successfully.")
        else:
            print(f"Attempt {i+1}: No transmission.")

    print("\n--- CSMA/CD Summary ---")
    print(f"Total Attempts: {attempts}")
    print(f"Successful Transmissions: {success_count}")
    print(f"Collisions Detected: {collision_count}")
    print(f"Efficiency: {(success_count/attempts)*100:.2f}%")
    return success_count, collision_count


def csma_ca_simulation(stations, attempts):
    print("\n=== CSMA/CA (Collision Avoidance) Simulation ===")
    collision_count = 0
    success_count = 0

    for i in range(attempts):
        ready_stations = [s for s in range(stations) if random.random() < 0.4]
        if len(ready_stations) > 1:
            # Stations perform random backoff before transmission
            chosen = random.choice(ready_stations)
            print(f"Attempt {i+1}: Stations {ready_stations} ready, Station {chosen} wins after backoff.")
            success_count += 1
        elif len(ready_stations) == 1:
            success_count += 1
            print(f"Attempt {i+1}: Station {ready_stations[0]} transmitted successfully.")
        else:
            print(f"Attempt {i+1}: No transmission.")

    print("\n--- CSMA/CA Summary ---")
    print(f"Total Attempts: {attempts}")
    print(f"Successful Transmissions: {success_count}")
    print(f"Collisions Avoided: {attempts - success_count}")
    print(f"Efficiency: {(success_count/attempts)*100:.2f}%")
    return success_count, attempts - success_count


def main():
    print("\n=== Performance Analysis of CSMA/CD and CSMA/CA ===")
    stations = int(input("Enter number of stations: "))
    attempts = int(input("Enter number of transmission attempts: "))

    print("\nSimulating CSMA/CD and CSMA/CA protocols...\n")

    cd_success, cd_collisions = csma_cd_simulation(stations, attempts)
    ca_success, ca_collisions = csma_ca_simulation(stations, attempts)

    print("\n=== Final Performance Comparison ===")
    print(f"CSMA/CD - Efficiency: {(cd_success/attempts)*100:.2f}% | Collisions: {cd_collisions}")
    print(f"CSMA/CA - Efficiency: {(ca_success/attempts)*100:.2f}% | Collisions Avoided: {ca_collisions}")

    if cd_success > ca_success:
        print("\n📊 Result: CSMA/CD performed better in this simulation.")
    else:
        print("\n📊 Result: CSMA/CA performed better in this simulation.")


if __name__ == "__main__":
    main()



