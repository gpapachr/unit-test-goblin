from enum import Enum

class SmellType(str, Enum):
    NO_ASSERTIONS = "no-assertions"
    TODO_ANNOTATION = "todo-annotation"