import pytest

from python_library_boilerplate.constants.codes import CODE_ERROR_INTERNAL_LIBRARY
from python_library_boilerplate.constants.messages import MESSAGE_ERROR_INTERNAL_LIBRARY
from python_library_boilerplate.utils.exceptions import (
    AuthenticationError,
    BaseError,
    BusinessError,
    ConflictError,
    InternalError,
    NotFoundError,
    ValidationError,
)


class TestBaseError:
    @pytest.mark.unit
    def test_default_code(self) -> None:
        error: BaseError = BaseError()
        assert error.code == CODE_ERROR_INTERNAL_LIBRARY

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: BaseError = BaseError()
        assert error.message == MESSAGE_ERROR_INTERNAL_LIBRARY

    @pytest.mark.unit
    def test_custom_code(self) -> None:
        error: BaseError = BaseError(code="CUSTOM_CODE")
        assert error.code == "CUSTOM_CODE"

    @pytest.mark.unit
    def test_custom_message(self) -> None:
        error: BaseError = BaseError(message="Custom message")
        assert error.message == "Custom message"

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: BaseError = BaseError(code="CUSTOM_CODE", message="Custom message")
        assert error.code == "CUSTOM_CODE"
        assert error.message == "Custom message"

    @pytest.mark.unit
    def test_inherits_from_exception(self) -> None:
        error: BaseError = BaseError()
        assert isinstance(error, Exception)

    @pytest.mark.unit
    def test_str_representation_uses_message(self) -> None:
        error: BaseError = BaseError(message="Test error")
        assert str(error) == "Test error"

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseError):
            raise BaseError()


class TestValidationError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        error: ValidationError = ValidationError()
        assert isinstance(error, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: ValidationError = ValidationError()
        assert error.message == "Validation error"

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: ValidationError = ValidationError(code="VAL_CODE", message="Invalid input")
        assert error.code == "VAL_CODE"
        assert error.message == "Invalid input"

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ValidationError):
            raise ValidationError()


class TestAuthenticationError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        error: AuthenticationError = AuthenticationError()
        assert isinstance(error, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: AuthenticationError = AuthenticationError()
        assert error.message == "Authentication error"

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(AuthenticationError):
            raise AuthenticationError()


class TestNotFoundError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        error: NotFoundError = NotFoundError()
        assert isinstance(error, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: NotFoundError = NotFoundError()
        assert error.message == "Resource not found"

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(NotFoundError):
            raise NotFoundError()


class TestConflictError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        error: ConflictError = ConflictError()
        assert isinstance(error, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: ConflictError = ConflictError()
        assert error.message == "Conflict error"

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ConflictError):
            raise ConflictError()


class TestBusinessError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        error: BusinessError = BusinessError()
        assert isinstance(error, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: BusinessError = BusinessError()
        assert error.message == "Business rule violated"

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BusinessError):
            raise BusinessError()


class TestInternalError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        error: InternalError = InternalError()
        assert isinstance(error, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: InternalError = InternalError()
        assert error.message == "Internal error"

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(InternalError):
            raise InternalError()
