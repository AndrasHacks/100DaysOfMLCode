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


# Now in this maze problem will have the heuristic as
# "Get the lowest Manhattan Distance item from the frontier".
class GreedyBestFirstSearchFrontier():

    def __init__(self, manhattan_distances):
        self.frontier = []
        self.explored = []
        self.manhattan_distances = manhattan_distances

    def add(self, node):
        if node.state not in self.explored:
            self.frontier.append(node)
            self.explored.append(node.state)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        # get the min manhattan distance element
        min_index = 0
        first_x, first_y = self.frontier[0].state
        min_manhattan_dist = self.manhattan_distances[first_x][first_y]
        for i in range(len(self.frontier)):
            x, y = self.frontier[i].state
            current_manhattan_distance = self.manhattan_distances[x][y]
            if current_manhattan_distance < min_manhattan_dist:
                min_index = i
                min_manhattan_dist = current_manhattan_distance
        nodeToReturn = self.frontier[min_index]
        del self.frontier[min_index]
        return nodeToReturn


# A* search gets the node with the lowest h(n) + g(n) value
# This means, that it does not only consider the heuristic, but also
# the cost of getting to the node.
class AStarFrontier():
    def __init__(self, manhattan_distances):
        self.frontier = []
        self.explored = []
        self.manhattan_distances = manhattan_distances

    def empty(self):
        return len(self.frontier) == 0

    def add(self, node):
        if node.state not in self.explored:
            self.frontier.append(node)
            self.explored.append(node.state)

    def remove(self):
        min_index = 0
        first_x, first_y = self.frontier[0].state

        # We also consider here the cost of getting to the element, not only
        # the Manahattan Distance heuristics.
        min_heuristic_and_cost_value = self.manhattan_distances[first_x][first_y] + \
            self.frontier[0].path_cost
        for i in range(len(self.frontier)):
            x, y = self.frontier[i].state
            curr_hc_value = self.manhattan_distances[x][y] + \
                self.frontier[i].path_cost
            if curr_hc_value < min_heuristic_and_cost_value:
                min_index = i
                min_heuristic_and_cost_value = curr_hc_value
        nodeToReturn = self.frontier[min_index]
        del self.frontier[min_index]
        return nodeToReturn


class Maze:

    walls = []
    solution = []

    # Taxicab geometry:
    # https://xlinux.nist.gov/dads/HTML/manhattanDistance.html
    # |x1 - x2| + |y1 - y2|
    manhattan_distances = []

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

        # get all Manhattan distances
        goalx, goaly = self.goal
        for i in range(height):
            row = []
            for j in range(width):
                manhattan_dist = abs(goalx - i) + abs(goaly - j)
                row.append(manhattan_dist)
            self.manhattan_distances.append(row)

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
        # frontier = StackFrontier()
        # frontier = QueueFrontier()
        # frontier = GreedyBestFirstSearchFrontier(self.manhattan_distances)
        frontier = AStarFrontier(self.manhattan_distances)
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


def main():
    fileName = './maze2.txt'
    with open(fileName) as file:
        content = file.readlines()
    maze = Maze(content)
    print(maze.draw())
    steps_taken = maze.solve()
    print('Solution found in %d steps' % steps_taken)
    print(maze.draw())


if __name__ == "__main__":
    main()
