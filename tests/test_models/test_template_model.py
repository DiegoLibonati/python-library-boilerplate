import pytest
from pydantic import ValidationError as PydanticValidationError

from python_library_boilerplate.models.template_model import TemplateModel


class TestTemplateModel:
    @pytest.mark.unit
    def test_valid_name(self) -> None:
        model: TemplateModel = TemplateModel(name="test")
        assert model.name == "test"

    @pytest.mark.unit
    def test_name_is_stored_correctly(self) -> None:
        model: TemplateModel = TemplateModel(name="example")
        assert model.name == "example"

    @pytest.mark.unit
    def test_name_strips_surrounding_whitespace(self) -> None:
        model: TemplateModel = TemplateModel(name="  hello  ")
        assert model.name == "hello"

    @pytest.mark.unit
    def test_name_strips_leading_whitespace(self) -> None:
        model: TemplateModel = TemplateModel(name="  hello")
        assert model.name == "hello"

    @pytest.mark.unit
    def test_name_strips_trailing_whitespace(self) -> None:
        model: TemplateModel = TemplateModel(name="hello  ")
        assert model.name == "hello"

    @pytest.mark.unit
    def test_empty_string_raises_validation_error(self) -> None:
        with pytest.raises(PydanticValidationError):
            TemplateModel(name="")

    @pytest.mark.unit
    def test_whitespace_only_raises_validation_error(self) -> None:
        with pytest.raises(PydanticValidationError):
            TemplateModel(name="   ")

    @pytest.mark.unit
    def test_single_character_name(self) -> None:
        model: TemplateModel = TemplateModel(name="a")
        assert model.name == "a"

    @pytest.mark.unit
    def test_name_with_numbers(self) -> None:
        model: TemplateModel = TemplateModel(name="test123")
        assert model.name == "test123"

    @pytest.mark.unit
    def test_name_with_internal_spaces_preserved(self) -> None:
        model: TemplateModel = TemplateModel(name="hello world")
        assert model.name == "hello world"
