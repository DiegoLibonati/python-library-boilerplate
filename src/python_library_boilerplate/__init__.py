from importlib.metadata import PackageNotFoundError, version

from .template import Template

try:
    __version__ = version("python-library-boilerplate")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__all__ = ["Template", "__version__"]
