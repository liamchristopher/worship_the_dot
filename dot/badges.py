"""
Badge generation for THE DOT.

Creates badges and shields for repositories that worship THE DOT.
"""


def generate_worship_badge(format: str = "markdown") -> str:
    """Generate a badge showing THE DOT worship status."""
    badge_url = "https://img.shields.io/badge/Worships-THE%20DOT-red?style=flat-square&logo=git"

    if format == "markdown":
        return f"[![Worships THE DOT]({badge_url})](https://github.com/liamchristopher/worship_the_dot)"
    elif format == "html":
        return f'<a href="https://github.com/liamchristopher/worship_the_dot"><img src="{badge_url}" alt="Worships THE DOT"></a>'
    elif format == "rst":
        return f".. image:: {badge_url}\n   :target: https://github.com/liamchristopher/worship_the_dot"
    elif format == "url":
        return badge_url
    else:
        raise ValueError(f"Unknown format: {format}")


def generate_commit_badge(valid: bool, format: str = "markdown") -> str:
    """Generate a badge for commit validation status."""
    if valid:
        badge_url = "https://img.shields.io/badge/commits-worship%20THE%20DOT-brightgreen?style=flat-square"
        alt_text = "Valid Commits"
    else:
        badge_url = "https://img.shields.io/badge/commits-invalid-red?style=flat-square"
        alt_text = "Invalid Commits"

    if format == "markdown":
        return f"![{alt_text}]({badge_url})"
    elif format == "html":
        return f'<img src="{badge_url}" alt="{alt_text}">'
    elif format == "rst":
        return f".. image:: {badge_url}\n   :alt: {alt_text}"
    elif format == "url":
        return badge_url
    else:
        raise ValueError(f"Unknown format: {format}")


def generate_all_badges(format: str = "markdown") -> str:
    """Generate all THE DOT badges."""
    worship = generate_worship_badge(format)
    commit = generate_commit_badge(True, format)

    if format in ["markdown", "rst"]:
        return f"{worship}\n{commit}"
    elif format == "html":
        return f"{worship}\n<br>\n{commit}"
    else:
        return f"{worship}\n{commit}"
