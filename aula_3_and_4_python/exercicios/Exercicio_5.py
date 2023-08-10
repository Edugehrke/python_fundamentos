


class Triangulo:
    
    def __init__(self, lado_1, lado_2, lado_3): 
        self._lado_1 = lado_1
        self._lado_2 = lado_2
        self._lado_3 = lado_3
        print('Objeto instanciado com sucesso! ')


    def eh_valido(self):
        lado_1_valido = self._lado_3 + self._lado_2 > self._lado_1
        lado_2_valido = self._lado_1 + self._lado_3 > self._lado_2
        lado_3_valido = self._lado_1 + self._lado_2 > self._lado_3

        return lado_1_valido is True and lado_2_valido is True and lado_3_valido is True
    
    
    def calcula_perimetro(self):
        return self._lado_1 + self._lado_2 + self._lado_3
    
    def tipo_triangulo(self):
        if self._lado_1 == self._lado_2 == self._lado_3:
            print('Este triangulo é equilatero')
        
        elif(self._lado_1 != self._lado_2) and (self._lado_1 != self._lado_3) and (self._lado_2 != self._lado_3):
            print('Escaleno')

        else:
            print('Isoceles')



if __name__ == '__main__':
    triangulo_1 = Triangulo(4,6,7)
    triangulo_2 = Triangulo(3,3,3)
    triangulo_3 = Triangulo(3,3,5)

    print(triangulo_1.eh_valido())
    print(triangulo_2.eh_valido())

    print(triangulo_1.calcula_perimetro())
    print(triangulo_2.calcula_perimetro())

    triangulo_1.tipo_triangulo()
    triangulo_2.tipo_triangulo()
    triangulo_3.tipo_triangulo()



