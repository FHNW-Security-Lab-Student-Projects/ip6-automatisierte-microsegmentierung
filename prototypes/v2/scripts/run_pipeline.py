from microseg.constraints.parser import parse_constraints, group_constraints
from microseg.constraints.parser import parse_constraints
from microseg.topology.builder import TopologyBuilder
from microseg.topology.graph import pretty_print_graph
from microseg.graph.path_engine import PathEngine


def main():
    # ---------------------------
    # Load Constrains
    # ---------------------------
    constraints = parse_constraints("datasets/synthetic/simple_scenario.json")

    # grouped = group_constraints(constraints)
    # for group_name, items in grouped.items():
    #     print(f"\n=== {group_name.upper()} ===")
    #     for c in items:
    #         print(c)

    # ---------------------------
    # Build Graph
    # ---------------------------
    builder = TopologyBuilder(constraints)
    graph = builder.build()

    # pretty_print_graph(graph.get_nodes(), graph.get_edges())

    # ---------------------------
    # Graph Engine
    # ---------------------------
    engine = PathEngine(graph)

    print(engine.get_path("User1", "User2"))
    print(engine.get_path("User1", "User3"))
    print(engine.get_path("User2", "User3"))
    print(engine.get_path("User1", "Switch01"))
    print(engine.get_path("User1", "Switch02"))
    
        
    print(engine.is_reachable("User1", "User2"))
    print(engine.is_reachable("User1", "User3"))
    print(engine.is_reachable("User2", "User3"))




if __name__ == "__main__":
    main()
