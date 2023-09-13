""" 
2 pontos) O trecho de co ́digo a seguir deve imprimir os valores 
listados abaixo. Com-
plete a chamada recursiva g(???) da fun ̧ca ̃o g(a,b).

def g (a,b):
    
    if len(a)<b:return [a] 
    return [a[:b]]+g(???)

print (g(list(range(10)),3)) print (g("x" * 10 ,4))

[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]] 
["xxxx", "xxxx", "xx"]

"""

def g (a,b):
    if len(a)<b:return [a]
    return [a[:b]]+g(a[b:],b)

#print (g(list(range(10)),3))
print (g("*"*10,4))