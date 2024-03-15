
"""
**Test Suite for the `CPU` Class (from `app.models.inventory`):**

This test suite verifies the functionality of the `CPU` class, focusing on:

* **CPU Creation:**
    * `test_create_cpu`: Ensures a `CPU` object is created with correct initial values from a provided dictionary.
    * `test_create_invalid_cores`: Tests that invalid values for the `cores` attribute raise appropriate exceptions using `pytest.mark.parametrize`. Validates integer types (TypeError for non-integers) and range (ValueError for negative or zero cores).

**Fixtures:**

* `cpu_values`: Provides a dictionary with default CPU attributes for test cases.
* `cpu`: Creates a `CPU` object using the `cpu_values` fixture.

**Test Data:**

* `test_create_invalid_cores` uses `pytest.mark.parametrize` to efficiently test multiple scenarios with different invalid core values.
"""

import pytest

from app.models import inventory as i

@pytest.fixture
def cpu_values():
    return {
        "name" : "RYZEN Threadripper 2990WX",
        "manufacturer" : "AMD",
        "total" : 10,
        "allocated" : 3,
        "cores" : 32,
        "socket" : "sTR4",
        "power_watts" : 250
    }


@pytest.fixture
def cpu(cpu_values):
    return i.CPU(**cpu_values)

class Test_CUP():

    def test_create_cpu(self, cpu,cpu_values):
        for attr_name, value in cpu_values.items():
            assert getattr(cpu,attr_name) == value
        

    @pytest.mark.parametrize(
        "cores_test, exception", [(10.5, TypeError), (-1, ValueError), (0,ValueError)]
    )
    def test_create_invalid_cores(self,cores_test, exception, cpu_values):
        cpu_values["cores"] = cores_test
        with pytest.raises(exception):
            i.CPU(**cpu_values)
