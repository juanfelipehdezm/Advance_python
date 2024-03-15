"""
Tests the validator functions
Command line: python -m pytest tests (this should be executed on the root directory)

Tests for the `validate_integer` function within the `app.utils.validators` module.

**Test Cases:**

* `test_valid`: Ensures that the function accepts valid integer values within the specified range.
* `test_type_error`: Asserts that the function raises a `TypeError` when a non-integer value is provided.
* `test_min_err_msg`: Verifies that the function raises a `ValueError` with the expected message when the argument value is below the minimum allowed value.
* `test_max_err_msg`: Verifies that the function raises a `ValueError` with the expected message when the argument value is above the maximum allowed value.
"""
import pytest

from app.utils.validators import validate_integer

class Test_Integer_Validator:
    def test_valid(self):
        validate_integer("arg", 10,0,20)

    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_integer("arg",1.5)


    def test_min_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("arg",10, 100)
        assert "arg" in str(ex.value)
        assert "100" in str(ex.value)

    def test_max_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("arg",arg_value=300, max_value=100)
        assert "arg" in str(ex.value)
        assert "100" in str(ex.value)


