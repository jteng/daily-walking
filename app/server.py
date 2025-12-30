"""Simple static file server for the project.

This uses Python's standard library so no external dependencies are required.
It serves files from the current working directory, which lets it serve the
existing `index.html` at the repo root.

Usage:
    python -m app.server  # serves on port 8000
    from app.server import run_server
    run_server(port=8080)
"""

from __future__ import annotations

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


def run_server(port: int = 8001) -> None:
    """Run a simple HTTP server serving the current working directory.

    Args:
        port: TCP port to bind to. Defaults to 8000.
    """
    addr = ("0.0.0.0", port)
    handler = SimpleHTTPRequestHandler
    httpd = ThreadingHTTPServer(addr, handler)
    print(f"Serving HTTP on {addr[0]} port {addr[1]} (http://{addr[0]}:{addr[1]}/) ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, shutting down server")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run_server()
