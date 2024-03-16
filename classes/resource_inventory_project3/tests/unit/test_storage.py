"""
**Test Suite for the `Storage` Class (from `app.models.inventory`):**

This test suite verifies the functionality of the `Storage` class, focusing on:

* **Storage Creation:**
    * `test_create`: Ensures a `Storage` object is created with correct initial values from a provided dictionary.

**Fixtures:**

* `storage_values`: Provides a dictionary with default storage attributes for test cases.
* `storage`: Creates a `Storage` object using the `storage_values` fixture.

"""

from app.models import inventory as i
import pytest

@pytest.fixture
def storage_values():
    return {
        "name" : "Thumbdrive",
        "manufacturer" : "Sandisk",
        "total" : 10,
        "allocated" : 3,
        "capacity_gb" : 250
    }

@pytest.fixture
def storage(storage_values):
    return i.Storage(**storage_values)

class Test_Storage():
    def test_create(self, storage_values, storage):
        for attr_name, value in storage_values.items():
            assert getattr(storage,attr_name) == value