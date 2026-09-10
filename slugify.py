import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Convert an arbitrary string into a URL-friendly slug."""
    lowered = text.lower()
    hyphenated = _NON_ALNUM.sub("-", lowered)
    return hyphenated.strip("-")
