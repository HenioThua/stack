import stack
import size

def test_size():
    p1 = stack.stack()
    p2 = stack.stack()
    p1.push(1)
    p1.push(2)
    p1.push(3)
    x = size.size(p1, p2)
    assert x == 3

def test_p1_n_esta_vazio():
    p1 = stack.stack()
    p2 = stack.stack()
    p1.push(1)
    p1.push(2)
    p1.push(3)
    x = size.size(p1, p2)
    assert not p1.isEmpty()

def test_p2_ta_vazio():
    p1 = stack.stack()
    p2 = stack.stack()
    p1.push(1)
    p1.push(2)
    p1.push(3)
    x = size.size(p1, p2)
    assert p2.isEmpty()

    
def test_p1_ta_igual():
    p1 = stack.stack()
    p2 = stack.stack()
    p1.push(1)
    p1.push(2)
    p1.push(3)
    x = size.size(p1, p2)
    p1test = p1.pop()
    p1test2 = p1.pop()
    p1test3 = p1.pop()
    assert p1test == 3 and p1test2 == 2 and p1test3 == 1 
    































