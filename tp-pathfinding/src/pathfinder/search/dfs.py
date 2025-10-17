from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        # Nodo raíz
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Caso trivial: ya estamos en el objetivo
        if grid.objective_test(root.state):
            return Solution(root)

        # Frontera tipo pila (DFS)
        frontera = StackFrontier()
        frontera.add(root)

        # Conjunto de visitados para evitar ciclos (versión grafo)
        explorados = set()

        while True:
            if frontera.is_empty():
                return NoSolution()

            nodo_actual = frontera.remove()  # saca el último agregado (LIFO)

            # Evitar repetir estados
            if nodo_actual.state in explorados:
                continue
            explorados.add(nodo_actual.state)

            # Expandir sucesores
            for accion in grid.actions(nodo_actual.state):
                estado_sucesor = grid.result(nodo_actual.state, accion)
                nodo_sucesor = Node(
                    "",
                    state=estado_sucesor,
                    parent=nodo_actual,
                    action=accion,
                    cost=nodo_actual.cost + grid.individual_cost(nodo_actual.state, accion),
                )
                if grid.objective_test(estado_sucesor):
                    return Solution(nodo_sucesor, explorados)
                frontera.add(nodo_sucesor)
