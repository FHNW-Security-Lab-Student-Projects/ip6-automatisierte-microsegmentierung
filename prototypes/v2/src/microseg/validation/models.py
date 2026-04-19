class ValidationResult:
    def __init__(self):
        self.allow_violations = []
        self.deny_violations = []

    def is_valid(self):
        return not self.allow_violations and not self.deny_violations

    def __str__(self):
        lines = []

        if self.is_valid():
            return "Validation: SUCCESS"

        lines.append("Validation: FAILED")

        if self.allow_violations:
            lines.append("\nALLOW Violations:")
            for v in self.allow_violations:
                lines.append(f"  - {v}")

        if self.deny_violations:
            lines.append("\nDENY Violations:")
            for v in self.deny_violations:
                lines.append(f"  - {v}")

        return "\n".join(lines)
