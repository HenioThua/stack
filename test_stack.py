import stack


def test_empty():
    x = stack.stack()
    assert x.isEmpty()

def test_push_not_empty():
    y = stack.stack()
    y.push(10)
    assert not y.isEmpty()
def test_pop():
    z = stack.stack()
    z.push(12)
    z.pop()
    assert z.isEmpty()

def test_bota_e_tira():
    pilha = stack.stack()
    pilha.push(17)
    pilhaR = pilha.pop()
    assert pilhaR == 17
