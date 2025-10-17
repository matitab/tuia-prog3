from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        #grid -> problema a solucionar
        #search(grid) -> devuelve Solución o NoSolución
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        if grid.objective_test(root.state):
            return Solution(root, reached={root.state})
        frontera = QueueFrontier()
        frontera.add(root)
        reached = {root.state}
        while True:
            if frontera.is_empty():
                return NoSolution(reached)
            nodo_nuevo = frontera.remove()
            for casilla in grid.actions(nodo_nuevo.state):
                estado_sucesor = grid.result(nodo_nuevo.state, casilla)
                if estado_sucesor in reached:
                    continue
                reached.add(estado_sucesor)
                nuevo_costo = nodo_nuevo.cost + grid.individual_cost(nodo_nuevo.state, casilla)
                nodo_sucesor = Node("", state=estado_sucesor, cost=nuevo_costo, parent=nodo_nuevo, action=casilla)
                if grid.objective_test(estado_sucesor):
                    return Solution(nodo_sucesor, reached)
                frontera.add(nodo_sucesor)