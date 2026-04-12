import logging

import pytest

from python_library_boilerplate.configs.logger_config import setup_logger


class TestSetupLogger:
    @pytest.mark.unit
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-instance")
        assert isinstance(logger, logging.Logger)

    @pytest.mark.unit
    def test_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "python-library-boilerplate"

    @pytest.mark.unit
    def test_custom_name(self) -> None:
        logger: logging.Logger = setup_logger("custom-logger-name")
        assert logger.name == "custom-logger-name"

    @pytest.mark.unit
    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-debug-level")
        assert logger.level == logging.DEBUG

    @pytest.mark.unit
    def test_logger_has_at_least_one_handler(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-has-handler")
        assert len(logger.handlers) > 0

    @pytest.mark.unit
    def test_handler_is_stream_handler(self) -> None:
        logger: logging.Logger = setup_logger("test-logger-stream-handler")
        assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)

    @pytest.mark.unit
    def test_no_duplicate_handlers_on_repeated_calls(self) -> None:
        name: str = "test-logger-no-duplicate"
        logger1: logging.Logger = setup_logger(name)
        count_after_first: int = len(logger1.handlers)
        logger2: logging.Logger = setup_logger(name)
        count_after_second: int = len(logger2.handlers)
        assert count_after_first == count_after_second

    @pytest.mark.unit
    def test_same_logger_instance_returned_for_same_name(self) -> None:
        name: str = "test-logger-same-instance"
        logger1: logging.Logger = setup_logger(name)
        logger2: logging.Logger = setup_logger(name)
        assert logger1 is logger2
