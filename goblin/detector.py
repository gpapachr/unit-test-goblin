from goblin.smell_types import SmellType

def smell_no_assertions(method):
    if method.assertion_count == 0:
        return SmellType.NO_ASSERTIONS

def smell_todo_annotation(method):
    if "TODO" in [a.upper() for a in method.annotations]:
        return SmellType.TODO_ANNOTATION

# New smell detectors:
def smell_disabled(method):
    if "DISABLED" in [a.upper() for a in method.annotations]:
        return SmellType.DISABLED

def smell_no_annotation(method):
    if "test" in method.method_name.lower() and not method.annotations:
        return SmellType.MISSING_ANNOTATION

# List of all rule functions
SMELL_RULES = [
    smell_no_assertions,
    smell_todo_annotation,
    smell_disabled,
    smell_no_annotation
]

def detect_smells(method):
    smells = []
    for rule in SMELL_RULES:
        result = rule(method)
        if result:
            smells.append(result)
    return smells