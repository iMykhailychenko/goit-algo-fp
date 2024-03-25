import heapq
import networkx as nx
from tabulate import tabulate

cities = [
    "Kyiv",
    "Paris",
    "Berlin",
    "Rome",
    "Madrid",
    "London",
    "Amsterdam",
    "Prague",
    "Vienna",
]


edges = [
    ("Kyiv", "Prague", 1389),
    ("Kyiv", "Vienna", 1514),
    ("Kyiv", "Berlin", 1292),
    ("Paris", "London", 344),
    ("Paris", "Berlin", 878),
    ("Paris", "Rome", 1423),
    ("Paris", "Madrid", 1054),
    ("Berlin", "Amsterdam", 577),
    ("Berlin", "Prague", 280),
    ("Berlin", "Vienna", 524),
    ("Rome", "Vienna", 766),
    ("Madrid", "Paris", 1054),
    ("London", "Amsterdam", 357),
    ("Amsterdam", "Prague", 708),
    ("Prague", "Vienna", 251),
]


positions = {
    "Kyiv": (18, 7),
    "Berlin": (9, 8.1),
    "Amsterdam": (5, 7.5),
    "London": (1, 8),
    "Paris": (3, 6),
    "Rome": (7.6, 1),
    "Madrid": (0, 0),
    "Prague": (9, 6),
    "Vienna": (10, 4),
}


G = nx.Graph()

for A, B, weight in edges:
    G.add_edge(A, B, weight=weight)


def dijkstra(start):
    distances = {}

    queue = [(start, 0)]
    distances[start] = 0

    while queue:
        (node, size) = heapq.heappop(queue)

        for neighbor in G[node]:
            new_size = size + G[node][neighbor].get("weight", 1)
            if neighbor not in distances or new_size < distances[neighbor]:
                distances[neighbor] = new_size
                heapq.heappush(queue, (neighbor, new_size))

    return distances


if __name__ == "__main__":
    data = []

    for city in cities:
        result = sorted(list(dijkstra(city).items()), key=lambda x: x[1])
        row = [f"{x[0]} ({x[1]})" for x in result]
        row.append(sum(x for _, x in result))
        data.append(row)

    print(f"Найкоротші шлях: {min(data, key=lambda x: x[-1])[-1]}", end="\n\n")
    print(tabulate(data, tablefmt="pipe"))
