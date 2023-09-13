""" 
1. (2 pontos) O trecho de coódigo a seguir deve imprimir o valor listado abaixo. 
Complete a função add de modo que isso ocorra.

class C(object):
    def __init__ (self ,a,b):
        self.a = a self.b=b
    def __add__ (self, c):
        return C(???, self.b+c.b)
    def __epr__(self): 
        return self .a+self .b

print (C(”ABC” , ”DEF”)+C(” foo ” , ”bar ”))

rabCBADEFbar

"""

class C(object):
   def __init__(self,a,b):
       self.a = a
       self.b = b
   def __add__(self, c):
       return C((self.a+c.b)[::-1], self.b+c.b)
   def __repr__(self):
       return self.a+self.b
                                                          
print (C("ABC","DEF")+C("foo", "bar"))
