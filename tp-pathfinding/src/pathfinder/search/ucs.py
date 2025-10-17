from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class UniformCostSearch:
    @staticmethod
    def search(problem):
        start = problem.initial
        frontier = PriorityQueueFrontier()
        start_node = Node(value="", state=start, cost=0, parent=None, action=None)
        frontier.add(start_node, 0)

        reached = {start: start_node}

        while not frontier.is_empty():
            node = frontier.pop()

            # Si llegamos al objetivo
            if problem.objective_test(node.state):
                return Solution(node, reached)

            # Expandir sucesores
            for action in problem.actions(node.state):
                child_state = problem.result(node.state, action)
                child_cost = node.cost + problem.individual_cost(node.state, action)
                child_node = Node(value="", state=child_state, cost=child_cost, parent=node, action=action)

                if (child_state not in reached) or (child_cost < reached[child_state].cost):
                    reached[child_state] = child_node
                    frontier.add(child_node, child_node.cost)

        return NoSolution()