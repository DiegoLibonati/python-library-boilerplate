import pytest

from template_library_python.constants.codes import CODE_ERROR_INTERNAL_LIBRARY, CODE_NOT_FOUND_TEMPLATE, CODE_NOT_VALID_INTEGER
from template_library_python.constants.messages import MESSAGE_ERROR_INTERNAL_LIBRARY, MESSAGE_NOT_FOUND_TEMPLATE, MESSAGE_NOT_VALID_INTEGER
from template_library_python.utils.exceptions import (
    AuthenticationError,
    BaseError,
    BusinessError,
    ConflictError,
    InternalError,
    NotFoundError,
    ValidationError,
)


class TestBaseError:
    def test_is_exception(self) -> None:
        assert issubclass(BaseError, Exception)

    def test_default_code(self) -> None:
        error = BaseError()
        assert error.code == CODE_ERROR_INTERNAL_LIBRARY

    def test_default_message(self) -> None:
        error = BaseError()
        assert error.message == MESSAGE_ERROR_INTERNAL_LIBRARY

    def test_custom_code(self) -> None:
        error = BaseError(code="CUSTOM_CODE")
        assert error.code == "CUSTOM_CODE"

    def test_custom_message(self) -> None:
        error = BaseError(message="Custom message")
        assert error.message == "Custom message"

    def test_str_representation_is_message(self) -> None:
        error = BaseError(message="Custom message")
        assert str(error) == "Custom message"

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseError):
            raise BaseError()


class TestValidationError:
    def test_is_base_error(self) -> None:
        assert issubclass(ValidationError, BaseError)

    def test_default_message(self) -> None:
        error = ValidationError()
        assert error.message == "Validation error"

    def test_custom_code_and_message(self) -> None:
        error = ValidationError(code=CODE_NOT_VALID_INTEGER, message=MESSAGE_NOT_VALID_INTEGER)
        assert error.code == CODE_NOT_VALID_INTEGER
        assert error.message == MESSAGE_NOT_VALID_INTEGER

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ValidationError):
            raise ValidationError()

    def test_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ValidationError()


class TestAuthenticationError:
    def test_is_base_error(self) -> None:
        assert issubclass(AuthenticationError, BaseError)

    def test_default_message(self) -> None:
        error = AuthenticationError()
        assert error.message == "Authentication error"

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(AuthenticationError):
            raise AuthenticationError()


class TestNotFoundError:
    def test_is_base_error(self) -> None:
        assert issubclass(NotFoundError, BaseError)

    def test_default_message(self) -> None:
        error = NotFoundError()
        assert error.message == "Resource not found"

    def test_custom_code_and_message(self) -> None:
        error = NotFoundError(code=CODE_NOT_FOUND_TEMPLATE, message=MESSAGE_NOT_FOUND_TEMPLATE)
        assert error.code == CODE_NOT_FOUND_TEMPLATE
        assert error.message == MESSAGE_NOT_FOUND_TEMPLATE

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(NotFoundError):
            raise NotFoundError()


class TestConflictError:
    def test_is_base_error(self) -> None:
        assert issubclass(ConflictError, BaseError)

    def test_default_message(self) -> None:
        error = ConflictError()
        assert error.message == "Conflict error"

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ConflictError):
            raise ConflictError()


class TestBusinessError:
    def test_is_base_error(self) -> None:
        assert issubclass(BusinessError, BaseError)

    def test_default_message(self) -> None:
        error = BusinessError()
        assert error.message == "Business rule violated"

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BusinessError):
            raise BusinessError()


class TestInternalError:
    def test_is_base_error(self) -> None:
        assert issubclass(InternalError, BaseError)

    def test_default_message(self) -> None:
        error = InternalError()
        assert error.message == "Internal error"

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(InternalError):
            raise InternalError()
