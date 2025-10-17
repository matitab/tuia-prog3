from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def manhattan(state: tuple[int, int], objetivo: tuple[int, int]) -> int:
    return abs(state[0] - objetivo[0]) + abs(state[1] - objetivo[1])

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid, h=manhattan) -> Solution:
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        if grid.objective_test(root.state):
            return Solution(root, reached={root.state})
        frontera = PriorityQueueFrontier()
        frontera.add(root, h(root.state, grid.end))
        reached = {root.state}
        while not frontera.is_empty():
            nodo_nuevo = frontera.pop()
            for casilla in grid.actions(nodo_nuevo.state):
                estado_sucesor = grid.result(nodo_nuevo.state, casilla)
                if estado_sucesor in reached:
                    continue
                reached.add(estado_sucesor)
                nuevo_costo = nodo_nuevo.cost + grid.individual_cost(nodo_nuevo.state, casilla)
                nodo_sucesor = Node("", state=estado_sucesor, cost=nuevo_costo, parent=nodo_nuevo, action=casilla)
                if grid.objective_test(estado_sucesor):
                    return Solution(nodo_sucesor, reached)
                frontera.add(nodo_sucesor, h(estado_sucesor, grid.end))
        return NoSolution(reached)
