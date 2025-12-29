"""Minimal tests for the project.

This test only checks that `app.server` can be imported and exposes
`run_server` so we catch syntax/import errors early.
"""


def test_app_server_importable():
    import importlib

    mod = importlib.import_module("app.server")
    assert hasattr(mod, "run_server"), "app.server should expose run_server"
