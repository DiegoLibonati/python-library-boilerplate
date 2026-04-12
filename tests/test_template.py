import pytest

from python_library_boilerplate.constants.codes import CODE_NOT_FOUND_TEMPLATE, CODE_NOT_VALID_INTEGER
from python_library_boilerplate.constants.messages import MESSAGE_NOT_FOUND_TEMPLATE, MESSAGE_NOT_VALID_INTEGER
from python_library_boilerplate.models.template_model import TemplateModel
from python_library_boilerplate.template import Template
from python_library_boilerplate.utils.exceptions import NotFoundError, ValidationError


class TestTemplateInit:
    @pytest.mark.unit
    def test_name_is_stored(self) -> None:
        t: Template = Template(name="Die")
        assert t.name == "Die"

    @pytest.mark.unit
    def test_name_can_be_any_string(self) -> None:
        t: Template = Template(name="some-library")
        assert t.name == "some-library"


class TestTemplatePydanticModel:
    @pytest.mark.unit
    def test_returns_template_model(self, template: Template) -> None:
        result: TemplateModel = template.pydantic_model
        assert isinstance(result, TemplateModel)

    @pytest.mark.unit
    def test_model_name_matches_instance_name(self, template: Template) -> None:
        result: TemplateModel = template.pydantic_model
        assert result.name == template.name

    @pytest.mark.unit
    def test_property_returns_equal_models_on_repeated_calls(self, template: Template) -> None:
        model1: TemplateModel = template.pydantic_model
        model2: TemplateModel = template.pydantic_model
        assert model1 == model2


class TestTemplateSayHello:
    @pytest.mark.unit
    def test_say_hello_returns_none(self, template: Template) -> None:
        result: None = template.say_hello()
        assert result is None


class TestTemplateThrowNotFound:
    @pytest.mark.unit
    def test_raises_not_found_error(self, template: Template) -> None:
        with pytest.raises(NotFoundError):
            template.throw_not_found()

    @pytest.mark.unit
    def test_error_code(self, template: Template) -> None:
        with pytest.raises(NotFoundError) as exc_info:
            template.throw_not_found()
        assert exc_info.value.code == CODE_NOT_FOUND_TEMPLATE

    @pytest.mark.unit
    def test_error_message(self, template: Template) -> None:
        with pytest.raises(NotFoundError) as exc_info:
            template.throw_not_found()
        assert exc_info.value.message == MESSAGE_NOT_FOUND_TEMPLATE


class TestTemplateAdd:
    @pytest.mark.unit
    def test_add_two_positive_integers(self, template: Template) -> None:
        result: int = template.add(1, 2)
        assert result == 3

    @pytest.mark.unit
    def test_add_zero(self, template: Template) -> None:
        result: int = template.add(0, 0)
        assert result == 0

    @pytest.mark.unit
    def test_add_negative_integers(self, template: Template) -> None:
        result: int = template.add(-1, -2)
        assert result == -3

    @pytest.mark.unit
    def test_add_positive_and_negative(self, template: Template) -> None:
        result: int = template.add(5, -3)
        assert result == 2

    @pytest.mark.unit
    def test_add_large_numbers(self, template: Template) -> None:
        result: int = template.add(1000000, 2000000)
        assert result == 3000000

    @pytest.mark.unit
    def test_add_float_raises_validation_error(self, template: Template) -> None:
        with pytest.raises(ValidationError):
            template.add(1.5, 2)  # type: ignore[arg-type]

    @pytest.mark.unit
    def test_add_string_raises_validation_error(self, template: Template) -> None:
        with pytest.raises(ValidationError):
            template.add("1", 2)  # type: ignore[arg-type]

    @pytest.mark.unit
    def test_add_none_raises_validation_error(self, template: Template) -> None:
        with pytest.raises(ValidationError):
            template.add(None, 2)  # type: ignore[arg-type]

    @pytest.mark.unit
    def test_add_validation_error_code(self, template: Template) -> None:
        with pytest.raises(ValidationError) as exc_info:
            template.add("x", 1)  # type: ignore[arg-type]
        assert exc_info.value.code == CODE_NOT_VALID_INTEGER

    @pytest.mark.unit
    def test_add_validation_error_message(self, template: Template) -> None:
        with pytest.raises(ValidationError) as exc_info:
            template.add("x", 1)  # type: ignore[arg-type]
        assert exc_info.value.message == MESSAGE_NOT_VALID_INTEGER
