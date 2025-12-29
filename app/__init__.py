"""app package for the project.

This package contains a tiny HTTP server to serve the existing index.html
from the repository root. Keeping it a package makes imports in tests simple.
"""

__all__ = ["server"]
