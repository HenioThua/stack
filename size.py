import stack

def size(p1, p2):
    cont = 0

    while not p1.isEmpty():
       p2.push(p1.pop())
       cont += 1
    while not p2.isEmpty():
        p1.push(p2.pop())
    return cont
    
