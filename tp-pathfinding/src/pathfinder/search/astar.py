from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def manhattan(node: Node, estado_objetivo: tuple) -> int:
    return abs(node.state[0] - estado_objetivo[0]) + abs(node.state[1] - estado_objetivo[1])

class AStarSearch:
    @staticmethod
    def search(grid: Grid, h=None) -> Solution:
        if h is None:
            h = lambda node: manhattan(node, grid.end)
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        frontera = PriorityQueueFrontier()
        frontera.add(root, root.cost + h(root))
        reached = {}
        reached[root.state] = root.cost
        while True:
            if frontera.is_empty():
                return NoSolution(reached)
            n = frontera.pop()
            if grid.objective_test(n.state):
                return Solution(n, reached)
            for a in grid.actions(n.state): # por cada acción
                s = grid.result(n.state, a) # casilla resultante
                c = n.cost + grid.individual_cost(n.state, a)
                if s not in reached or c < reached[s]:
                    nodo_sucesor = Node("", state=s, parent=n, action=a, cost=c)
                    reached[s] = c
                    frontera.add(nodo_sucesor, nodo_sucesor.cost + h(nodo_sucesor))