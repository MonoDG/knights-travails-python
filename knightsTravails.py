class Node:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.distance = None
        self.predecessor = None
        self.neighbors = []

class KnightsTravails:
    ROWS = 8
    COLS = 8
    knight_movements = [[2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
    
    def __init__(self) -> None:
        self.adjacency_list = self.create_adjacency_list()

    def is_valid_movement(self, x, y):
        return x >= 0 and x < self.ROWS and y >= 0 and y < self.COLS

    def create_adjacency_list(self):
        adj_list = []
        for i in range(self.ROWS):
            nodes = []
            for j in range(self.COLS):
                nodes.append(Node(i, j))
            adj_list.append(nodes)

        for i in range(self.ROWS):
            for j in range(self.COLS):
                node = adj_list[i][j]
                for movement in self.knight_movements:
                    newRowX = i + movement[0]
                    newColY = j + movement[1]
                    
                    if self.is_valid_movement(newRowX, newColY):
                        node.neighbors.append(adj_list[newRowX][newColY])

        return adj_list
    
    def do_bfs(self, sourceX, sourceY, destX, destY):
        path = []
        queue = []

        (self.adjacency_list[sourceX][sourceY]).distance = 0
        queue.append(self.adjacency_list[sourceX][sourceY])

        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node.x == destX and current_node.y == destY:
                path.append(current_node)
                while current_node.predecessor != None:
                    path.append(current_node.predecessor)
                    current_node = current_node.predecessor
                path.reverse()
                return path
            
            for neighbor in current_node.neighbors:
                if neighbor.distance == None:
                    neighbor.distance = current_node.distance + 1
                    neighbor.predecessor = current_node
                    queue.append(neighbor)

        return path
    
if __name__ == "__main__":
    knights_travails = KnightsTravails()
    solution = knights_travails.do_bfs(0, 0, 7, 7)

    print(f"You made it in {len(solution) - 1} moves! Here's your path:")
    for step in solution:
        print(f"Node[{step.x},{step.y}] -> distance: {step.distance}, predecessor: {step.predecessor}")