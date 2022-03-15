from pathlib import Path

import setuptools_scm


def get_version() -> str:
    try:
        return setuptools_scm.get_version()
    except Exception:
        pass

    try:
        return Path(__file__).parent.joinpath("version.txt").read_text().strip("\n")
    except FileNotFoundError:
        return "0.0.0-unknown"


__version__ = get_version()
