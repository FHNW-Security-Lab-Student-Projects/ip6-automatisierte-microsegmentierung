from microseg.constraints.parser import parse_constraints, group_constraints


def main():
    # ---------------------------
    # Load Constrains
    # ---------------------------
    constraints = parse_constraints("datasets/synthetic/constrains.json")
    grouped = group_constraints(constraints)

    for group_name, items in grouped.items():
        print(f"\n=== {group_name.upper()} ===")
        for c in items:
            print(c)


if __name__ == "__main__":
    main()
