"""Demo entry point for the python-library-boilerplate library.

Run with:
    python -m examples.demo
or (if installed via `pip install -e .`):
    python_library_boilerplate-demo
"""

from python_library_boilerplate import Template
from python_library_boilerplate.configs.logger_config import setup_logger

logger = setup_logger("examples")


def main() -> None:
    name: str = "Die"
    library = Template(name=name)

    library.say_hello()

    result = library.add(num1=1, num2=2)
    logger.info(f"Sum: {result}")

    logger.info(f"Model: {type(library.pydantic_model)}")


if __name__ == "__main__":
    main()
