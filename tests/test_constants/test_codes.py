import pytest

from python_library_boilerplate.constants.codes import (
    CODE_ERROR_GENERIC,
    CODE_ERROR_INTERNAL_LIBRARY,
    CODE_NOT_FOUND_TEMPLATE,
    CODE_NOT_VALID_INTEGER,
)


class TestCodes:
    @pytest.mark.unit
    def test_code_error_internal_library_value(self) -> None:
        assert CODE_ERROR_INTERNAL_LIBRARY == "ERROR_INTERNAL_LIBRARY"

    @pytest.mark.unit
    def test_code_error_generic_value(self) -> None:
        assert CODE_ERROR_GENERIC == "ERROR_GENERIC"

    @pytest.mark.unit
    def test_code_not_valid_integer_value(self) -> None:
        assert CODE_NOT_VALID_INTEGER == "NOT_VALID_INTEGER"

    @pytest.mark.unit
    def test_code_not_found_template_value(self) -> None:
        assert CODE_NOT_FOUND_TEMPLATE == "NOT_FOUND_TEMPLATE"

    @pytest.mark.unit
    def test_all_codes_are_strings(self) -> None:
        codes: list[str] = [
            CODE_ERROR_INTERNAL_LIBRARY,
            CODE_ERROR_GENERIC,
            CODE_NOT_VALID_INTEGER,
            CODE_NOT_FOUND_TEMPLATE,
        ]
        for code in codes:
            assert isinstance(code, str)

    @pytest.mark.unit
    def test_all_codes_are_non_empty(self) -> None:
        codes: list[str] = [
            CODE_ERROR_INTERNAL_LIBRARY,
            CODE_ERROR_GENERIC,
            CODE_NOT_VALID_INTEGER,
            CODE_NOT_FOUND_TEMPLATE,
        ]
        for code in codes:
            assert len(code) > 0
