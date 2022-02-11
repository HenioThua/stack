import stack
import pytest
import transfer


def test_transfer_():
    p1 = stack.stack()
    p2 = stack.stack()
    p1.push(1)
    p1.push(2)
    p1.push(3)
    transfer.transfer(p1, p2)
    assert p1.isEmpty()

def test_transfer_enesimo():
    p1 = stack.stack()
    p2 = stack.stack()
    p1.push(1)
    p1.push(2)
    p1.push(3)
    transfer.transfer_enesimo(2, p1, p2)
    assert p2.pop() == 2
    
