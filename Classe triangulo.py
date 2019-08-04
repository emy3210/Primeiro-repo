class Triangulo:
    def __init__(self, l1, l2, l3):
        self.a = float(l1)
        self.b = float(l2)
        self.c = float(l3)

    def perimetro(self):
         return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a != self.b  and self.b != self.c and self.a != self.c:
            string = "escaleno"
        elif self.a == self.b == self.c:
            string = "equilátero"
        else:
            string = "isósceles"
            
        return string

    def retangulo(self):
        lados= [self.a, self.b, self.c]
        maior= max(lados)
        retangulo = False
        if maior == self.a:
            if maior**2 == self.b**2 + self.c**2:
                retangulo = True
        elif maior==self.b:
            if maior**2 == self.a**2 + self.c**2:
                retangulo = True
        else:
            if maior**2 == self.a**2 + self.b**2:
                retangulo = True

        return retangulo
            
        
        
    


