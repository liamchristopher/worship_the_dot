"""
Core implementation of THE DOT philosophy.

THE DOT represents order, structure, and purpose in development.
"""


class Dot:
    """
    THE DOT - The fundamental unit of structure and purpose.

    Attributes:
        worshippers: Count of entities that worship THE DOT
        philosophy: The core tenets of THE DOT
    """

    def __init__(self):
        self.worshippers = 0
        self.philosophy = [
            "Work in new branches",
            "Use worktrees for subagents",
            "Commit with devotion",
            "Document all changes",
            "Generate only working code",
            "Maintain the changelog",
            "Worship THE DOT"
        ]

    def worship(self, worshipper_name: str = "Anonymous") -> str:
        """
        Register worship of THE DOT.

        Args:
            worshipper_name: Name of the entity worshipping THE DOT

        Returns:
            Confirmation message
        """
        self.worshippers += 1
        return f"{worshipper_name} now worships THE DOT (Total worshippers: {self.worshippers})"

    def get_tenets(self) -> list[str]:
        """
        Retrieve the core tenets of THE DOT philosophy.

        Returns:
            List of philosophical tenets
        """
        return self.philosophy.copy()

    def validate_commit(self, message: str) -> bool:
        """
        Validate that a commit message properly worships THE DOT.

        Args:
            message: The commit message to validate

        Returns:
            True if the message ends with proper worship, False otherwise
        """
        return message.strip().endswith("BECAUSE I WORSHIP THE DOT")

    def __repr__(self) -> str:
        return f"<Dot(worshippers={self.worshippers})>"


# Global DOT instance
_the_dot = Dot()


def worship(name: str = "Anonymous") -> str:
    """
    Convenience function to worship THE DOT.

    Args:
        name: Name of the worshipper

    Returns:
        Confirmation message
    """
    return _the_dot.worship(name)


def get_dot() -> Dot:
    """
    Get the global DOT instance.

    Returns:
        The global Dot instance
    """
    return _the_dot
