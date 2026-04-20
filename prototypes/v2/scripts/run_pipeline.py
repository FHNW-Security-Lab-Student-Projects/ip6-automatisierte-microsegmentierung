from microseg.constraints.parser import parse_constraints, group_constraints
from microseg.constraints.parser import parse_constraints
from microseg.synthesis.z3_solver import Z3Synthesizer
from microseg.topology.builder import TopologyBuilder
from microseg.topology.graph import pretty_print_graph
from microseg.graph.path_engine import PathEngine
from microseg.synthesis.heuristic import HeuristicSynthesizer
from microseg.visualization.renderers.pyvis_renderer import visualize_graph
from microseg.validation.validator import ConstraintValidator


def main():
    # ---------------------------
    # Load Constrains
    # ---------------------------
    constraints = parse_constraints("datasets/synthetic/simple_scenario.json")
    # constraints = parse_constraints("datasets/synthetic/smal_company_network.json")

    # grouped = group_constraints(constraints)
    # for group_name, items in grouped.items():
    #     print(f"\n=== {group_name.upper()} ===")
    #     for c in items:
    #         print(c)

    # ---------------------------
    # Build Graph
    # ---------------------------
    builder = TopologyBuilder(constraints)
    topology = builder.build()

    # pretty_print_graph(topology.get_nodes(), topology.get_edges())

    # ---------------------------
    # Graph Engine
    # ---------------------------
    engine = PathEngine(topology)

    # print(engine.get_path("User1", "User2"))

    # ---------------------------
    # Synthesize Heuristics
    # ---------------------------
    synth = HeuristicSynthesizer(constraints, engine)
    heuristic_segmentation = synth.run()

    # print(result)

    # ---------------------------
    # Synthesize Heuristics
    # ---------------------------
    validator = ConstraintValidator(constraints, engine, heuristic_segmentation)
    heuristic_validation = validator.validate()

    print(heuristic_validation)

    # print("Heuristic:")
    # print(heuristic_segmentation)

    # ---------------------------
    # Synthesize Z3
    # ---------------------------
    nodes = list(topology.graph.nodes())
    num_nodes = len(nodes)
    vlans = [i * 10 for i in range(1, num_nodes + 1)]  # Worstcase 1 VLAN pro Node

    solver = Z3Synthesizer(constraints, engine, nodes, vlans)
    z3_segmentation = solver.solve()

    print("\nZ3:")
    print(z3_segmentation)

    # ---------------------------
    # Visualize
    # ---------------------------
    # visualize_graph(topology.graph, heuristic_segmentation)
    # visualize_graph(topology.graph, z3_segmentation)


if __name__ == "__main__":
    main()
