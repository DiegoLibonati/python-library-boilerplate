from template_library_python.constants.messages import (
    MESSAGE_ERROR_GENERIC,
    MESSAGE_ERROR_INTERNAL_LIBRARY,
    MESSAGE_NOT_FOUND_TEMPLATE,
    MESSAGE_NOT_VALID_INTEGER,
)


class TestErrorMessages:
    def test_message_error_internal_library_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_INTERNAL_LIBRARY, str)

    def test_message_error_internal_library_value(self) -> None:
        assert MESSAGE_ERROR_INTERNAL_LIBRARY == "Internal library error."

    def test_message_error_generic_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_GENERIC, str)

    def test_message_error_generic_value(self) -> None:
        assert MESSAGE_ERROR_GENERIC == "Generic error."


class TestNotValidMessages:
    def test_message_not_valid_integer_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_INTEGER, str)

    def test_message_not_valid_integer_value(self) -> None:
        assert MESSAGE_NOT_VALID_INTEGER == "The value entered is not a valid integer."


class TestNotFoundMessages:
    def test_message_not_found_template_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_TEMPLATE, str)

    def test_message_not_found_template_value(self) -> None:
        assert MESSAGE_NOT_FOUND_TEMPLATE == "No template found."
