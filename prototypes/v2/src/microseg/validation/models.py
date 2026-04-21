class ValidationResult:
    def __init__(self):
        """
        Track validation issues: separate lists for ALLOW and DENY violations.
        """

        self.allow_violations = []
        self.deny_violations = []

    def is_valid(self):
        """
        Return True if no violations exist.
        """

        return not self.allow_violations and not self.deny_violations

    def __str__(self):
        """
        Return formatted validation summary; includes violations if present.
        """

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
