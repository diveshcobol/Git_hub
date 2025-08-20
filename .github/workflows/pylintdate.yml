import re
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class EnforceYYYYMMDDChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "enforce-yyyymmdd"
    msgs = {
        "W9004": (
            "Date string '%s' is not in yyyymmdd format",
            "invalid-date-format",
            "Use yyyymmdd format for dates, not ddmmyyyy or others.",
        ),
    }

    def visit_const(self, node):
        """
        Visit all constants (like string literals).
        """
        if isinstance(node.value, str):
            val = node.value

            # Match 8-digit strings (possible dates)
            if re.fullmatch(r"\d{8}", val):
                year, month, day = int(val[0:4]), int(val[4:6]), int(val[6:8])

                # Accept only if it looks like a valid YYYYMMDD date
                if not (1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31):
                    self.add_message("invalid-date-format", node=node, args=(val,))

                # Reject if it looks like DDMMYYYY (day first)
                elif int(val[0:2]) <= 31 and int(val[2:4]) <= 12:
                    # If it's not starting with year, treat as wrong
                    if year < 1000:  # quick sanity check
                        self.add_message("invalid-date-format", node=node, args=(val,))


def register(linter):
    linter.register_checker(EnforceYYYYMMDDChecker(linter))
