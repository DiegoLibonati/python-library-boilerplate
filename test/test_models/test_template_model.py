import pytest
from pydantic import ValidationError as PydanticValidationError

from template_library_python.models.template_model import TemplateModel


class TestTemplateModelValidName:
    def test_valid_name(self) -> None:
        model = TemplateModel(name="Diego")
        assert model.name == "Diego"

    def test_name_is_string(self) -> None:
        model = TemplateModel(name="Diego")
        assert isinstance(model.name, str)

    def test_name_with_spaces_inside(self) -> None:
        model = TemplateModel(name="Diego Martin")
        assert model.name == "Diego Martin"


class TestTemplateModelStripping:
    def test_name_strips_leading_whitespace(self) -> None:
        model = TemplateModel(name="  Diego")
        assert model.name == "Diego"

    def test_name_strips_trailing_whitespace(self) -> None:
        model = TemplateModel(name="Diego  ")
        assert model.name == "Diego"

    def test_name_strips_both_sides(self) -> None:
        model = TemplateModel(name="  Diego  ")
        assert model.name == "Diego"


class TestTemplateModelInvalidName:
    def test_empty_string_raises(self) -> None:
        with pytest.raises(PydanticValidationError):
            TemplateModel(name="")

    def test_whitespace_only_raises(self) -> None:
        with pytest.raises(PydanticValidationError):
            TemplateModel(name="   ")

    def test_missing_name_raises(self) -> None:
        with pytest.raises(PydanticValidationError):
            TemplateModel()
