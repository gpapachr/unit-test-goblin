from goblin.smell_types import SmellType

def detect_smells(test_method):
    smells = []

    if test_method.assertion_count == 0:
        smells.append(SmellType.NO_ASSERTIONS)

    if "TODO" in [a.upper() for a in test_method.annotations]:
        smells.append(SmellType.TODO_ANNOTATION)

    return smells