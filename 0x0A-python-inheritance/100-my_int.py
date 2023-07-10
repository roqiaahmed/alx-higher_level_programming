"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, other):
        """Override == opeartor with != behavior."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override != operator with == behavior."""
        return not super().__ne__(other)
