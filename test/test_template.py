import logging

import pytest

from template_library_python.constants.codes import CODE_NOT_FOUND_TEMPLATE, CODE_NOT_VALID_INTEGER
from template_library_python.constants.messages import MESSAGE_NOT_FOUND_TEMPLATE, MESSAGE_NOT_VALID_INTEGER
from template_library_python.models.template_model import TemplateModel
from template_library_python.template import Template
from template_library_python.utils.exceptions import NotFoundError, ValidationError


class TestTemplateInit:
    def test_stores_name(self, template: Template, template_name: str) -> None:
        assert template.name == template_name

    def test_name_is_string(self, template: Template) -> None:
        assert isinstance(template.name, str)


class TestTemplatePydanticModel:
    def test_returns_template_model(self, template: Template) -> None:
        assert isinstance(template.pydantic_model, TemplateModel)

    def test_model_name_matches(self, template: Template, template_name: str) -> None:
        assert template.pydantic_model.name == template_name

    def test_each_call_returns_new_instance(self, template: Template) -> None:
        assert template.pydantic_model is not template.pydantic_model


class TestTemplateSayHello:
    def test_say_hello_logs_name(self, template: Template, template_name: str, caplog: pytest.LogCaptureFixture) -> None:
        with caplog.at_level(logging.INFO):
            template.say_hello()
        assert template_name in caplog.text

    def test_say_hello_returns_none(self, template: Template) -> None:
        assert template.say_hello() is None


class TestTemplateThrowNotFound:
    def test_raises_not_found_error(self, template: Template) -> None:
        with pytest.raises(NotFoundError):
            template.throw_not_found()

    def test_error_code_is_correct(self, template: Template) -> None:
        with pytest.raises(NotFoundError) as exc_info:
            template.throw_not_found()
        assert exc_info.value.code == CODE_NOT_FOUND_TEMPLATE

    def test_error_message_is_correct(self, template: Template) -> None:
        with pytest.raises(NotFoundError) as exc_info:
            template.throw_not_found()
        assert exc_info.value.message == MESSAGE_NOT_FOUND_TEMPLATE


class TestTemplateAdd:
    def test_sum_two_integers(self, template: Template) -> None:
        assert template.add(1, 2) == 3

    def test_sum_negative_numbers(self, template: Template) -> None:
        assert template.add(-3, -2) == -5

    def test_sum_zero(self, template: Template) -> None:
        assert template.add(0, 0) == 0

    def test_sum_returns_integer(self, template: Template) -> None:
        assert isinstance(template.add(1, 2), int)

    def test_sum_float_raises_validation_error(self, template: Template) -> None:
        with pytest.raises(ValidationError):
            template.add(1.5, 2)

    def test_sum_string_raises_validation_error(self, template: Template) -> None:
        with pytest.raises(ValidationError):
            template.add("1", 2)

    def test_sum_none_raises_validation_error(self, template: Template) -> None:
        with pytest.raises(ValidationError):
            template.add(None, 2)

    def test_sum_validation_error_code(self, template: Template) -> None:
        with pytest.raises(ValidationError) as exc_info:
            template.add(1.5, 2)
        assert exc_info.value.code == CODE_NOT_VALID_INTEGER

    def test_sum_validation_error_message(self, template: Template) -> None:
        with pytest.raises(ValidationError) as exc_info:
            template.add(1.5, 2)
        assert exc_info.value.message == MESSAGE_NOT_VALID_INTEGER
