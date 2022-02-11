import size
import stack
def transfer(p1, p2):
    sizeV = size.size(p1, p2)
    for i in range ( sizeV, 0, -1 ):
        transfer_enesimo( i, p1, p2)
        
        
    
    












def transfer_enesimo(n, p1, p2):
    for i in range (n -1):
        p2.push(p1.pop())
    p2F = p1.pop()
    for i in range (n -1):
        p1.push(p2.pop())
    p2.push(p2F)
    
