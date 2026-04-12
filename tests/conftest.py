import pytest

from python_library_boilerplate.template import Template


@pytest.fixture(scope="function")
def template() -> Template:
    return Template(name="test")
