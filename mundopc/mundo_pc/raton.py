from mundo_pc.dispositivo_entrada import Dispositivo_entrada


class Raton(Dispositivo_entrada):

    contador_ratones=0

    def __init__(self,marca,tipo_entrada):
        Raton.contador_ratones+=1
        self._id_raton=Raton.contador_ratones
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return f'ID {self._id_raton} Marca:{self._marca} Tipo de entrada: {self._tipo_entrada}'

if __name__== '__main__':
        raton1= Raton('hp','usb')
        print(raton1)
        raton2= Raton('ibm','bluetooh')
        print(raton2)