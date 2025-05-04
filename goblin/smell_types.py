from enum import Enum


class SmellType(str, Enum):
    NO_ASSERTIONS = "no-assertions"
    TODO_ANNOTATION = "todo-annotation"
    DISABLED = "disabled-annotation"
    IGNORED = "ignore-annotation"
    MISSING_TEST_ANNOTATION = "missing-test-annotation"