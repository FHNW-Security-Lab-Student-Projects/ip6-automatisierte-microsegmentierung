from microseg.constraints.models import AllowConstraint

from .types import ConstraintType


class ConstraintExpander:
    def __init__(self, constraints, groups):
        self.constraints = constraints
        self.groups = groups

    def expand(self):
        expanded = []

        for group_name, members in self.groups.items():
            members = list(members)

            for i in range(len(members)):
                for j in range(i + 1, len(members)):
                    a = members[i]
                    b = members[j]

                    expanded.append(AllowConstraint(a, b))

        for c in self.constraints:
            if c.type in [ConstraintType.ALLOW, ConstraintType.DENY]:
                src_list = self.resolve(c.src)
                dst_list = self.resolve(c.dst)

                for src in src_list:
                    for dst in dst_list:
                        expanded.append(type(c)(src, dst))

            else:
                expanded.append(c)

        return expanded

    def resolve(self, entity):
        if entity in self.groups:
            return list(self.groups[entity])
        return [entity]
