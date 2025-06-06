import pytest
from goblin.detector import detect_smells
from goblin.smell_types import SmellType
from goblin.analyzer import TestMethod

CLASS_NAME = "TestClass"
METHOD_NAME = "testMethod"

def test_no_assertions_smell():
    method = TestMethod(
        class_name=CLASS_NAME,
        method_name=METHOD_NAME,
        annotations=["Test"],
        assertion_count=0
    )
    smells = detect_smells(method)
    assert SmellType.NO_ASSERTIONS in smells

def test_todo_annotation_smell():
    method = TestMethod(
        class_name=CLASS_NAME,
        method_name=METHOD_NAME,
        annotations=["TODO"],
        assertion_count=1
    )
    smells = detect_smells(method)
    assert SmellType.TODO_ANNOTATION in smells

def test_disabled_annotation_smell():
    method = TestMethod(
        class_name=CLASS_NAME,
        method_name=METHOD_NAME,
        annotations=["Disabled"],
        assertion_count=1
    )
    smells = detect_smells(method)
    assert SmellType.DISABLED in smells

def test_ignored_annotation_smell():
    method = TestMethod(
        class_name=CLASS_NAME,
        method_name=METHOD_NAME,
        annotations=["Ignore"],
        assertion_count=1
    )
    smells = detect_smells(method)
    assert SmellType.IGNORED in smells

def test_missing_test_annotation_smell():
    method = TestMethod(
        class_name=CLASS_NAME,
        method_name=METHOD_NAME,
        annotations=[],
        assertion_count=1
    )
    smells = detect_smells(method)
    assert SmellType.MISSING_TEST_ANNOTATION in smells

def test_multiple_smells():
    method = TestMethod(
        class_name=CLASS_NAME,
        method_name=METHOD_NAME,
        annotations=["TODO", "Disabled", "Test"],
        assertion_count=0
    )
    smells = detect_smells(method)
    assert SmellType.NO_ASSERTIONS in smells
    assert SmellType.TODO_ANNOTATION in smells
    assert SmellType.DISABLED in smells

def test_no_smells():
    method = TestMethod(
        class_name=CLASS_NAME,
        method_name=METHOD_NAME,
        annotations=["Test"],
        assertion_count=1
    )
    smells = detect_smells(method)
    assert not smells  # Should be an empty set