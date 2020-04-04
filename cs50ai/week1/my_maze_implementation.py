class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


class Frontier():
    def __init__(self):
        self.frontier = []
        self.explored = []

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        popped = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return popped


class StackFrontier (Frontier):
    # Stack Frontier is for Depth First Search
    def add(self, node):
        if node.state not in self.explored:
            self.frontier.append(node)
            self.explored.append(node.state)


class QueueFrontier (Frontier):
    # QueueFrontier is for Breadth First Search
    def add(self, node):
        if node.state not in self.explored:
            self.frontier.insert(0, node)
            self.explored.append(node.state)


class Maze:

    walls = []
    solution = []

    def __init__(self, mazeContent):
        height = len(mazeContent)
        width = max(len(line) for line in mazeContent)

        for i in range(height):
            row = []
            for j in range(width):
                if mazeContent[i][j] == 'A':
                    self.start = (i, j)
                    row.append(False)
                elif mazeContent[i][j] == 'B':
                    self.goal = (i, j)
                    row.append(False)
                elif mazeContent[i][j] == ' ':
                    row.append(False)
                else:
                    row.append(True)
            self.walls.append(row)

    def draw(self):
        height = len(self.walls)
        width = max(len(l) for l in self.walls)

        s = ''
        for i in range(height):
            for j in range(width):
                if self.walls[i][j]:
                    s += '█'
                elif self.goal == (i, j):
                    s += 'B'
                elif self.start == (i, j):
                    s += 'A'
                elif (i, j) in self.solution:
                    s += '*'
                else:
                    s += ' '
            s += '\n'
        return s

    def solve(self):
        count_states_exoplored = 0
        frontier = StackFrontier()
        # frontier = QueueFrontier()
        frontier.add(Node(self.start, None, None, 0))

        while True:
            count_states_exoplored += 1

            if frontier.empty():
                raise NameError("Solution not found!")

            currentNode = frontier.remove()
            if currentNode.state == self.goal:
                while currentNode.parent != None:
                    self.solution.append(currentNode.state)
                    currentNode = currentNode.parent
                return count_states_exoplored

            neighbourNodes = self.getNeighbours(currentNode)
            for action, state in neighbourNodes:
                frontier.add(Node(state, currentNode, action,
                                  currentNode.path_cost + 1))

    def getNeighbours(self, node):
        row, column = node.state
        candidates = [
            ('up', (row - 1, column)),
            ('down', (row + 1, column)),
            ('left', (row, column - 1)),
            ('right', (row, column + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if r > -1 and r < len(self.walls) and c > -1 and c < (max(len(l) for l in self.walls)) and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result


fileName = './maze3.txt'
with open(fileName) as file:
    content = file.readlines()
maze = Maze(content)
print(maze.draw())
steps_taken = maze.solve()
print('Solution found in %d steps' % steps_taken)
print(maze.draw())
