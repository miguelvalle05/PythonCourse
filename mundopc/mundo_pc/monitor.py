class Monitor():

    contado_monitores=0

    def __init__(self,marca,tamaño):
        Monitor.contado_monitores+=1
        self._id_monitor=Monitor.contado_monitores
        self._marca=marca
        self._tamaño=tamaño

    def __str__(self):
        return f'ID {self._id_monitor} Marca: {self._marca} Tamaño:{self._tamaño}'

if __name__=='__main__':

    monitor1=Monitor('hp',15)
    print(monitor1)
    monitor2=Monitor('lenovo',23)
    print(monitor2)

