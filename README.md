# slugify

A tiny helper that convertes an arbitrary string into a URL-friendly "slug".

```python
from slugify import slugify

slugify("Hello, World!")        # -> "hello-world"
slugify("  Trailing spaces  ")  # -> "trailing-spaces"
```

## Rules

- Lowercase everything
- Replace any run of non-alphanumeric characters with a single hyphen
- Strip leading and trailing hyphens

## Running the tests

```bash
python -m pytest
```
