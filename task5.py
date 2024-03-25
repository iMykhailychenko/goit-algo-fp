import uuid
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class Node:
    def __init__(self, key, color="#0000FF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def get_hex_color(color, index):
    step = 12
    base_rgb = (int(color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
    return f"#{''.join(f'{min(255, c + index * step):02X}' for c in base_rgb)}"


def dfs(node, visited, color):
    if node:
        visited.add(node.id)
        node.color = get_hex_color(color, len(visited))
        dfs(node.left, visited, color)
        dfs(node.right, visited, color)


def bfs(node, color):
    if node:
        visited = set()
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current.id not in visited:
                visited.add(current.id)
                current.color = get_hex_color(color, len(visited))
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        left_x = x - 1 / 2**layer
        right_x = x + 1 / 2**layer
        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, left_x, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, right_x, y - 1, layer + 1)


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, node_size=2500, node_color=colors, arrows=False
    )
    plt.show()


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right = Node(5)
    root.right.left = Node(23)
    root.right.right = Node(2)
    root.left.left.left = Node(46)
    root.left.left.right = Node(21)
    root.left.right.left = Node(7)
    root.right.left.left = Node(11)
    root.right.left.right = Node(21)
    root.right.right.left = Node(22)
    root.right.right.right = Node(17)

    draw_tree(root)

    dfs(root, set(), root.color)
    draw_tree(root)

    bfs(root, root.color)
    draw_tree(root)
