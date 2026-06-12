from main import power
import  pytest



def testn_equals_zero():
    assert power(2,0)==1
    assert power(10,0)==1

def test_n_greater_than_zero():
    assert power(5,2)==25
    assert power(2,3)==8

def test_n_les_than_zero():
    assert power(2,-1)==0.5
    assert power(2,-2)==0.25
@pytest.mark.parametrize("x,n,expected",[
    (2,0,1),(10,0,1),(2,3,8),
    (5,2,25),(2,-1,0.5),(2,-2,0.25)
])
def test_all(x,n,expected):
    assert power(x,n) == expected