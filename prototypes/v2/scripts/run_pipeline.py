from microseg.constraints.parser import parse_constraints, group_constraints
from microseg.constraints.parser import parse_constraints
from microseg.synthesis.z3_solver import Z3Synthesizer
from microseg.topology.builder import TopologyBuilder
from microseg.topology.graph import pretty_print_graph
from microseg.graph.path_engine import PathEngine
from microseg.synthesis.heuristic import HeuristicSynthesizer
from microseg.visualization.renderers.pyvis_renderer import visualize_graph
from microseg.validation.validator import ConstraintValidator


def print_section(title):
    print(f"\n=== {title} ===")


def main():
    # ---------------------------
    # LOAD
    # ---------------------------
    print_section("LOAD")

    constraints = parse_constraints("datasets/synthetic/simple_scenario.json")
    # constraints = parse_constraints("datasets/synthetic/smal_company_network.json")
    print(f"Constraints loaded: {len(constraints)}")

    # ---------------------------
    # TOPOLOGY
    # ---------------------------
    print_section("TOPOLOGY")

    builder = TopologyBuilder(constraints)
    topology = builder.build()

    num_nodes = len(topology.graph.nodes())
    num_edges = len(topology.graph.edges())

    print(f"Nodes: {num_nodes}")
    print(f"Edges: {num_edges}")

    # ---------------------------
    # GRAPH ENGINE
    # ---------------------------
    engine = PathEngine(topology)

    # ---------------------------
    # HEURISTIC
    # ---------------------------
    print_section("HEURISTIC")

    synth = HeuristicSynthesizer(constraints, engine)
    heuristic_segmentation = synth.run()

    validator = ConstraintValidator(constraints, engine, heuristic_segmentation)
    heuristic_validation = validator.validate()

    if heuristic_validation.is_valid():
        print("Status: SUCCESS")
    else:
        print("Status: FAILED")
        print(heuristic_validation)

    # ---------------------------
    # Z3 SOLVER
    # ---------------------------
    print_section("Z3 SOLVER")

    nodes = list(topology.graph.nodes())
    vlans = [10, 20, 30, 40]

    solver = Z3Synthesizer(constraints, engine, nodes, vlans)
    z3_segmentation = solver.solve()

    if z3_segmentation:
        print("Status: SAT")
    else:
        print("Status: UNSAT (see conflicts above)")

    # ---------------------------
    # RESULT
    # ---------------------------
    print_section("RESULT")

    if heuristic_validation.is_valid():
        print("Heuristic Solution:")
        print(heuristic_segmentation)
    else:
        print("Heuristic Solution: INVALID")

    if z3_segmentation:
        print("\nZ3 Solution:")
        print(z3_segmentation)
    else:
        print("Z3 Solution: NONE")

    # ---------------------------
    # VISUALIZATION
    # ---------------------------
    print_section("VISUALIZATION")

    if heuristic_validation.is_valid():
        print("Rendering Heuristic...")
        visualize_graph(topology.graph, heuristic_segmentation)
    else:
        print("Skipping Heuristic (invalid)")

    if z3_segmentation:
        print("Rendering Z3...")
        visualize_graph(topology.graph, z3_segmentation)
    else:
        print("Skipping Z3 (no solution)")


if __name__ == "__main__":
    main()
