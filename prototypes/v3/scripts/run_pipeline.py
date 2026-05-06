from microseg.constraints.expander import ConstraintExpander
from microseg.constraints.parser import load_dataset
from microseg.synthesis.z3_solver import Z3Synthesizer
from microseg.topology.builder import TopologyBuilder
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

    # constraints, groups = load_dataset("datasets/synthetic/simple_scenario.json")
    # constraints, groups = load_dataset("datasets/synthetic/simple_scenario_unsat.json")
    constraints, groups = load_dataset("datasets/synthetic/smal_company_network.json")
    # constraints, groups = load_dataset("datasets/synthetic/smal_company_network_unsat.json")
    print(f"Constraints loaded: {len(constraints)}")

    # ---------------------------
    # EXPANSION
    # ---------------------------
    print_section("EXPANSION")

    expander = ConstraintExpander(constraints, groups)
    expanded_constraints = expander.expand()

    print(f"Expanded constraints: {len(expanded_constraints)}")

    constraints = expanded_constraints

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

    heuristic_segmentation = None
    heuristic_validation = None

    try:
        synth = HeuristicSynthesizer(constraints, engine)
        heuristic_segmentation = synth.run()

        heuristic_validator = ConstraintValidator(
            constraints, engine, heuristic_segmentation
        )
        heuristic_validation = heuristic_validator.validate()
        print("Status: SUCCESS")

    except Exception as e:
        print("Status: FAILED")
        print(f"Reason: {e}")

    # ---------------------------
    # Z3 SOLVER
    # ---------------------------
    print_section("Z3 SOLVER")

    nodes = list(topology.graph.nodes())
    vlans = [10, 20, 30, 40]

    solver = Z3Synthesizer(constraints, engine, nodes, vlans)
    z3_segmentation = solver.solve()

    if z3_segmentation is None:
        print("Status: UNSAT (no solution)")
        z3_validation = None

    else:
        z3_validator = ConstraintValidator(constraints, engine, z3_segmentation)
        z3_validation = z3_validator.validate()

        if z3_validation.is_valid():
            print("Status: SAT")
        else:
            print("Status: INVALID (unexpected)")

    # ---------------------------
    # RESULT
    # ---------------------------
    print_section("RESULT")

    # print("--- debug ----")
    # # pretty_print_graph(topology.graph.nodes, topology.graph.edges)
    # print(topology.graph.nodes)
    # print(topology.graph.edges)

    # print("--- debug ---- \n")

    # --- HEURISTIC ---
    if heuristic_segmentation is None:
        print("Heuristic Solution: NONE")

    elif heuristic_validation and heuristic_validation.is_valid():
        print("Heuristic Solution:")
        print(heuristic_segmentation)

    else:
        print("Heuristic Solution: INVALID")

    # --- Z3 ---
    if z3_segmentation is None:
        print("Z3 Solution: NONE")

    else:
        print("\nZ3 Solution:")
        print(z3_segmentation)

    # ---------------------------
    # VISUALIZATION
    # ---------------------------
    print_section("VISUALIZATION")

    # --- HEURISTIC ---
    if (
        heuristic_segmentation is not None
        and heuristic_validation
        and heuristic_validation.is_valid()
    ):
        print("Rendering Heuristic...")
        visualize_graph(topology.graph, heuristic_segmentation, "Heuristic")

    else:
        print("Skipping Heuristic (no valid solution)")

    # --- Z3 ---
    if z3_segmentation is not None:
        print("Rendering Z3...")
        visualize_graph(topology.graph, z3_segmentation, "Z3 Solver")

    else:
        print("Skipping Z3 (no solution)")


if __name__ == "__main__":
    main()
