#import unittest
#from IM01TestingDemo.Demo.main import is_prime


# class PrimeTestCase(unittest.TestCase):
#     def test_true(self):
#         self.assertTrue(is_prime(3))
#     def test_false(self):
#         self.assertFalse(is_prime(4))
#     def test_exception(self):
#         with self.assertRaises(ValueError):
#             is_prime(1)
# test white box



from main import is_prime
import pytest

def test_true():
    assert is_prime(3)== True

def test_false():
    assert is_prime(4) == False


@pytest.mark.parametrize('n,expected',[
    (2,True),(4,False),(143,False),
    (11,True),(97,True)
])
def test_others(n,expected):
    assert is_prime(n) == expected
def test_exception():
    with pytest.raises(ValueError):
        is_prime(1)
@pytest.mark.timeout(1)
def test_timeout():
    is_prime(9999)