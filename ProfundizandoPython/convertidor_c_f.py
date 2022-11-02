class ConvertidorRTemperatura:

    MAX_CELSIOUS=100
    MAX_FARENHEIT=213


    @classmethod
    def convertir_c_f(cls,celsious):
        if celsious>cls.MAX_CELSIOUS:
            raise ValueError(f'Temperatura en celsious demasiado alta {celsious}')
        return celsious*9/5 + 32

    @classmethod

    def convertir_f_c(cls,farenheit):
        if farenheit>cls.MAX_FARENHEIT:
            raise ValueError(f'Temperatura en farenheit demasiado alta {farenheit}')
        return (farenheit)-32*5/9


if __name__ == '__main__':
    resultado=ConvertidorRTemperatura.convertir_c_f(15)
    print(f'15C a F {resultado:.2f}')
    resultado = ConvertidorRTemperatura.convertir_f_c(59)
    print(f'59C a F {resultado:.2f}')