from flag_coverage_filtering.lib import add
from flag_coverage_filtering.lib2 import add2

def test_add_e2e():
    assert add(1, 2) == 3

def test_add_e2e_2():
    assert add2(1, 2) == 3
