"""Test for Resource class
command line: python -m pytest tests (this should be executed on the root directory)"""

import pytest

from app.models import inventory as i

@pytest.fixture
def resource_values():
    return {
        "name" : "Parrot",
        "manufacturer" : "Jungle",
        "total":100,
        "allocated": 50
    }

@pytest.fixture
def resource(resource_values):
    return i.Resource(**resource_values)

class Test_resourcer():

    def test_create_resource(self, resource):        
        assert resource.name == "Parrot"
        assert resource.manufacturer == "Jungle"
        assert resource.total == 100
        assert resource.allocated == 50


    @pytest.mark.parametrize("total,allocated",[("5", 50), (100, "10")])
    def test_create_invalid_int_type(self, resource, total, allocated):
        with pytest.raises(TypeError):
            resource.total = total
            resource.allocated = allocated

    @pytest.mark.parametrize("total,allocated",[(10, 5000), (-100, 0)])
    def test_create_invalid_int_value(self,total, allocated):
        with pytest.raises(ValueError):
            i.Resource("Parrot","Jungle", total, allocated)

    
    def test_claim(self,resource):
        n = 2
        original_total = resource.total
        original_allocated = resource.allocated
        resource.claim(n)

        assert resource.total == original_total
        assert resource.allocated == original_allocated + n