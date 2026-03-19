from template_library_python.constants.codes import (
    CODE_ERROR_GENERIC,
    CODE_ERROR_INTERNAL_LIBRARY,
    CODE_NOT_FOUND_TEMPLATE,
    CODE_NOT_VALID_INTEGER,
)


class TestErrorCodes:
    def test_code_error_internal_library_is_string(self) -> None:
        assert isinstance(CODE_ERROR_INTERNAL_LIBRARY, str)

    def test_code_error_internal_library_value(self) -> None:
        assert CODE_ERROR_INTERNAL_LIBRARY == "ERROR_INTERNAL_LIBRARY"

    def test_code_error_generic_is_string(self) -> None:
        assert isinstance(CODE_ERROR_GENERIC, str)

    def test_code_error_generic_value(self) -> None:
        assert CODE_ERROR_GENERIC == "ERROR_GENERIC"


class TestNotValidCodes:
    def test_code_not_valid_integer_is_string(self) -> None:
        assert isinstance(CODE_NOT_VALID_INTEGER, str)

    def test_code_not_valid_integer_value(self) -> None:
        assert CODE_NOT_VALID_INTEGER == "NOT_VALID_INTEGER"


class TestNotFoundCodes:
    def test_code_not_found_template_is_string(self) -> None:
        assert isinstance(CODE_NOT_FOUND_TEMPLATE, str)

    def test_code_not_found_template_value(self) -> None:
        assert CODE_NOT_FOUND_TEMPLATE == "NOT_FOUND_TEMPLATE"
