import pytest

from python_library_boilerplate.constants.messages import (
    MESSAGE_ERROR_GENERIC,
    MESSAGE_ERROR_INTERNAL_LIBRARY,
    MESSAGE_NOT_FOUND_TEMPLATE,
    MESSAGE_NOT_VALID_INTEGER,
)


class TestMessages:
    @pytest.mark.unit
    def test_message_error_internal_library_value(self) -> None:
        assert MESSAGE_ERROR_INTERNAL_LIBRARY == "Internal library error."

    @pytest.mark.unit
    def test_message_error_generic_value(self) -> None:
        assert MESSAGE_ERROR_GENERIC == "Generic error."

    @pytest.mark.unit
    def test_message_not_valid_integer_value(self) -> None:
        assert MESSAGE_NOT_VALID_INTEGER == "The value entered is not a valid integer."

    @pytest.mark.unit
    def test_message_not_found_template_value(self) -> None:
        assert MESSAGE_NOT_FOUND_TEMPLATE == "No template found."

    @pytest.mark.unit
    def test_all_messages_are_strings(self) -> None:
        messages: list[str] = [
            MESSAGE_ERROR_INTERNAL_LIBRARY,
            MESSAGE_ERROR_GENERIC,
            MESSAGE_NOT_VALID_INTEGER,
            MESSAGE_NOT_FOUND_TEMPLATE,
        ]
        for message in messages:
            assert isinstance(message, str)

    @pytest.mark.unit
    def test_all_messages_are_non_empty(self) -> None:
        messages: list[str] = [
            MESSAGE_ERROR_INTERNAL_LIBRARY,
            MESSAGE_ERROR_GENERIC,
            MESSAGE_NOT_VALID_INTEGER,
            MESSAGE_NOT_FOUND_TEMPLATE,
        ]
        for message in messages:
            assert len(message) > 0
