import pytest

from template_library_python.template import Template

TEMPLATE_NAME = "TestName"


@pytest.fixture
def template_name() -> str:
    return TEMPLATE_NAME


@pytest.fixture
def template(template_name: str) -> Template:
    return Template(name=template_name)
