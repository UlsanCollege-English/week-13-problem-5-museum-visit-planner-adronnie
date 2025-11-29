from collections import deque

def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.

    rooms: list of room name strings.
    doors: list of (a, b) pairs, each pair is an undirected door between rooms a and b.
    start: start room name.
    goal: goal room name.

    Return:
      - list of room names from start to goal (inclusive) for one shortest path,
      - [start] if start == goal,
      - [] if no path exists.
    """

    # Edge case: no rooms at all
    if not rooms:
        return [] if start != goal else []

    # If start and goal are the same, return immediately
    if start == goal:
        return [start]

    # Build adjacency list
    graph = {r: [] for r in rooms}
    for a, b in doors:
        # undirected door
        graph[a].append(b)
        graph[b].append(a)

    # BFS setup
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # BFS loop
    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # If goal was never reached → no path
    if goal not in parent:
        return []

    # Reconstruct path by following parents backward
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path


if __name__ == "__main__":
    rooms = ["Entrance", "Hall", "Gallery", "Cafe"]
    doors = [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")]
    print(shortest_path(rooms, doors, "Entrance", "Cafe"))
